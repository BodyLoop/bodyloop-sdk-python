"""A BodyLoop API client which logs in with a username and password.

The generated SDK expects a ready token, so this module adds the missing piece:
`LoginAuthenticatedClient` fetches a token on first use and refetches it shortly
before it expires. `authenticated_client()` hands out the shared instance.

The host and the credentials belong to the application, so it passes them in
once at startup:

    from bodyloop_client import authenticated_client, configure_client

    configure_client(base_url=HOST, username=USERNAME, password=PASSWORD)

    client = await authenticated_client()
    probands = await get_probands.asyncio(client=client)
"""

import asyncio
import base64
import json
import logging
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime, timedelta

import httpx

from bodyloop_sdk.client import AuthenticatedClient, Client
from bodyloop_sdk.client.api.authentification import (
    login_api_v2_authentification_token_post as login_endpoint,
)
from bodyloop_sdk.client.models import (
    BodyLoginApiV2AuthentificationTokenPost,
    Token,
)

LOGGER = logging.getLogger(__name__)

# Log in again this long before the token actually expires.
TOKEN_REFRESH_MARGIN = timedelta(seconds=60)

# Something that can produce a token, such as `login_with_password` — or, in a
# Panel application, the browser (see `bodyloop_client_panel`).
TokenSource = Callable[[], Awaitable[Token]]


def expiry_of_jwt(token: str) -> datetime | None:
    """Read the `exp` claim of a JWT, or `None` if there is none to read.

    The signature is deliberately not verified: this is our own token, and the
    expiry is only used to decide when to log in again — never to grant access.
    """

    try:
        payload = token.split(".")[1]
        claims = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))

        return datetime.fromtimestamp(claims["exp"], tz=UTC)

    except (IndexError, KeyError, TypeError, ValueError):
        return None


class _TokenAuth(httpx.Auth):
    """Authenticates every request, and retries once if the token is rejected.

    httpx drives this as a generator: it sends what we yield, hands us the
    response, and sends anything we yield after that. So a 401 can be answered
    with a fresh login and a second attempt, transparently to the caller.
    """

    def __init__(self, client: "LoginAuthenticatedClient") -> None:
        self._client = client

    async def async_auth_flow(self, request: httpx.Request):
        token = self._client.token
        request.headers[self._client.auth_header_name] = self._client.authorization(token)

        response = yield request

        if response.status_code != httpx.codes.UNAUTHORIZED:
            return

        # The token was rejected, however fresh we believed it to be: it may
        # have been revoked, or the host may have restarted. Log in and retry.
        await self._client.refresh_token(stale_token=token)

        request.headers[self._client.auth_header_name] = self._client.authorization(self._client.token)

        yield request


class LoginAuthenticatedClient(AuthenticatedClient):
    """An `AuthenticatedClient` which keeps itself logged in.

    The token is unknown at construction time, so it is fetched on first use —
    and fetched again once it is close to expiring. The expiry comes from the
    `exp` claim of the token itself, so one client can serve many requests
    instead of logging in for each of them.

    Should a token be rejected anyway, the request is retried once with a fresh
    one, so a revoked token or a restarted host costs a retry rather than an
    error.

    Call `ensure_token()` before handing the client to an API function, or just
    use the async context, which does it for you:

        async with LoginAuthenticatedClient(
            base_url=HOST, username=USERNAME, password=PASSWORD
        ) as client:
            probands = await get_probands.asyncio(client=client)
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: str,
        password: str,
        **kwargs,
    ) -> None:
        super().__init__(base_url=base_url, token="", **kwargs)

        self.username = username
        self.password = password

        # No token yet, so it is expired as far as `token_is_fresh` cares.
        self.token_expires_at = datetime.min.replace(tzinfo=UTC)
        self._login_lock = asyncio.Lock()

        # Where tokens come from, in order of preference. Logging in with the
        # credentials is the fallback, so it stays last.
        self.token_sources: list[TokenSource] = [self.login_with_password]

        # The name of the source which provided the current token.
        self.token_source_used: str | None = None

        # The SDK hands these to every httpx client it builds.
        self._httpx_args.setdefault("auth", _TokenAuth(self))

    def authorization(self, token: str) -> str:
        """The `Authorization` header value for a token."""

        return f"{self.prefix} {token}" if self.prefix else token

    @property
    def token_is_fresh(self) -> bool:
        """Whether the current token is good for a while yet."""

        return datetime.now(UTC) + TOKEN_REFRESH_MARGIN < self.token_expires_at

    async def ensure_token(self) -> None:
        """Log in, unless the current token is still fresh."""

        if self.token_is_fresh:
            return

        async with self._login_lock:
            # Another task may have logged in while we waited for the lock.
            if self.token_is_fresh:
                return

            self._apply_token(await self.login())

    async def refresh_token(self, stale_token: str) -> None:
        """Log in again, unless someone already replaced `stale_token`.

        Requests in flight tend to be rejected together, and they would all ask
        for a new token. Only the first of them needs to fetch one.
        """

        async with self._login_lock:
            if self.token != stale_token:
                return

            self._apply_token(await self.login())

    def prefer_token_source(self, source: TokenSource) -> None:
        """Ask `source` for the token before anything tried so far."""

        self.token_sources.insert(0, source)

    async def login(self) -> Token:
        """Get a token from the first source willing to provide one.

        A source that fails is not fatal — the next one is tried, so a token
        source that only works sometimes can sit in front of the credentials.
        """

        problems = []
        last_exception = None

        for source in self.token_sources:
            name = getattr(source, "__name__", repr(source))

            try:
                token = await source()

            except Exception as exception:
                # Some exceptions carry no message at all — a timeout, say.
                reason = str(exception) or type(exception).__name__

                LOGGER.warning("Token source %s failed: %s", name, reason)
                problems.append(f"{name}: {reason}")
                last_exception = exception

            else:
                self.token_source_used = name

                return token

        raise RuntimeError(f"No token source worked — {'; '.join(problems)}") from last_exception

    async def login_with_password(self) -> Token:
        """Request a token for the configured credentials."""

        async with Client(
            base_url=self._base_url,
            verify_ssl=self._verify_ssl,
            raise_on_unexpected_status=self.raise_on_unexpected_status,
        ) as client:
            result = await login_endpoint.asyncio(
                client=client,
                body=BodyLoginApiV2AuthentificationTokenPost(
                    grant_type="password",
                    username=self.username,
                    password=self.password,
                ),
            )

        if not isinstance(result, Token):
            raise RuntimeError(f"Login failed: {result}")

        return result

    def _apply_token(self, token: Token) -> None:
        self.token = token.access_token
        self.token_expires_at = expiry_of_jwt(token.access_token) or (
            datetime.now(UTC) + timedelta(seconds=token.expires_in)
        )

        # The base class only stamps the header while building an httpx client,
        # so an already built one still carries the previous token. Requests
        # made through `_TokenAuth` get the current one either way.
        header = self.authorization(self.token)
        self._headers[self.auth_header_name] = header

        for httpx_client in (self._client, self._async_client):
            if httpx_client is not None:
                httpx_client.headers[self.auth_header_name] = header

    async def __aenter__(self) -> "LoginAuthenticatedClient":
        await self.ensure_token()

        return await super().__aenter__()

    def __enter__(self) -> "LoginAuthenticatedClient":
        raise NotImplementedError("Logging in is asynchronous — use 'async with' instead of 'with'.")


# One client for the whole app: it holds the token and the connection pool,
# and both are worth keeping between requests.
CLIENT: LoginAuthenticatedClient | None = None


def new_client(
    *,
    base_url: str,
    username: str,
    password: str,
    **kwargs,
) -> LoginAuthenticatedClient:
    """Build a client of its own.

    Prefer this over `configure_client()` wherever a client must not be shared
    — one holding a token that belongs to a single browser session, say.
    """

    kwargs.setdefault("raise_on_unexpected_status", True)

    return LoginAuthenticatedClient(
        base_url=base_url,
        username=username,
        password=password,
        **kwargs,
    )


def configure_client(**kwargs) -> LoginAuthenticatedClient:
    """Set up the shared client. Call this once, at startup."""

    global CLIENT

    CLIENT = new_client(**kwargs)

    return CLIENT


async def authenticated_client() -> LoginAuthenticatedClient:
    """The shared client, with a token that is valid for a while yet."""

    if CLIENT is None:
        raise RuntimeError("No client yet — call configure_client() first.")

    await CLIENT.ensure_token()

    return CLIENT
