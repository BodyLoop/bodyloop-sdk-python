"""Let a Panel application take its token from the browser.

A browser that is already signed in to BodyLoop holds a refresh token in a
cookie. The cookie belongs to the browser, so only JavaScript running in the
page can trade it for an access token — which is what `BrowserTokenFetcher`
does, and what `browser_first_client()` puts in front of the credentials.

    from bodyloop_client_panel import browser_first_client

    client, token_fetcher = browser_first_client(
        base_url=HOST, username=USERNAME, password=PASSWORD
    )

    ...

    pn.Column(token_fetcher, ...).servable()

The fetcher has to be somewhere in the served layout, or its script never runs
and every attempt falls back to the credentials.

Two things are worth knowing about the token this yields. It belongs to one
browser session, so the client holding it must not be shared between sessions:
build it with `browser_first_client()` from the application script, which Panel
re-runs per session, rather than with `configure_client()`. And the page must
be served from the same origin as the API, since the script posts to a relative
URL and sends the cookie along.
"""

import asyncio
import logging

import panel as pn
import param

from bodyloop_sdk.bodyloop_client import LoginAuthenticatedClient, new_client
from bodyloop_sdk.client.models import Token

TOKEN_ENDPOINT = "/api/v2/authentification/token"

# How long the browser gets to answer before the credentials are used instead.
BROWSER_TOKEN_TIMEOUT = 5.0

LOGGER = logging.getLogger(__name__)


class BrowserTokenFetcher(pn.reactive.ReactiveHTML):
    """Invisible component that asks the browser for an access token.

    The refresh token lives in a cookie owned by the browser, so only
    JavaScript running inside the page can trade it for an access token. The
    result is synced back into :attr:`access_token` or :attr:`error`, which is
    what :meth:`fetch_token` awaits.

    Both parameters are cleared before every attempt so that two identical
    results in a row still register as a change.
    """

    access_token = param.String(default="", allow_None=True)
    expires_in = param.Integer(default=0)
    error = param.String(default="", allow_None=True)
    _trigger = param.Integer(default=0)

    width = 0
    height = 0
    margin = 0

    _template = '<div id="token_fetcher" style="display: none"></div>'

    _scripts = {
        "_trigger": f"""
        if (data._trigger === 0) {{ return; }}
        data.access_token = '';
        data.error = '';

        const body = new URLSearchParams({{
            grant_type: 'refresh_token',
            scope: '',
            client_id: '',
            client_secret: 'string',
        }});

        fetch('{TOKEN_ENDPOINT}', {{
            method: 'POST',
            headers: {{
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            }},
            credentials: 'include',
            body: body.toString(),
        }})
        .then(response => {{
            if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
            return response.json();
        }})
        .then(json => {{
            if (!json.access_token) throw new Error('response carried no access_token');
            data.expires_in = json.expires_in || 0;
            data.access_token = json.access_token;
        }})
        .catch(err => {{ data.error = err.message; }});
        """
    }

    async def fetch_token(self) -> Token:
        """Have the browser trade its cookie for a token.

        Raises if the browser reports a problem or stays silent, which is the
        signal for the client to fall back to the next token source.
        """

        if pn.state.curdoc is None:
            raise RuntimeError("no Panel session, so there is no browser to ask")

        loop = asyncio.get_running_loop()
        future = loop.create_future()

        def on_result(*events):
            for event in events:
                if future.done() or not event.new:
                    continue

                if event.name == "error":
                    future.set_exception(RuntimeError(event.new))
                else:
                    future.set_result(event.new)

        watcher = self.param.watch(on_result, ["access_token", "error"])

        try:
            self._trigger += 1

            # Without a browser to answer — an unrendered fetcher, a closed tab
            # — nothing would ever resolve the future.
            access_token = await asyncio.wait_for(future, BROWSER_TOKEN_TIMEOUT)

        finally:
            self.param.unwatch(watcher)

        return Token(
            access_token=access_token,
            token_type="bearer",
            expires_in=self.expires_in,
        )


def browser_first_client(
    **kwargs,
) -> tuple[LoginAuthenticatedClient, BrowserTokenFetcher]:
    """A client that asks the browser first and the credentials second.

    Returns the client together with the fetcher it needs; put the fetcher in
    the served layout.
    """

    client = new_client(**kwargs)
    token_fetcher = BrowserTokenFetcher()

    client.prefer_token_source(token_fetcher.fetch_token)

    return client, token_fetcher
