from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_apitoken_api_v2_authentification_users_username_api_token_post import (
    BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.token import Token
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: Any,
    *,
    body: BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/authentification/users/{username}/api_token".format(
            username=quote(str(username), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Token | None:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | Token]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: Any,
    *,
    client: AuthenticatedClient,
    body: BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset = UNSET,
) -> Response[HTTPValidationError | Token]:
    """Apitoken

     Request API token

    Args:
        username (Any):
        body (BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Token]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: Any,
    *,
    client: AuthenticatedClient,
    body: BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset = UNSET,
) -> HTTPValidationError | Token | None:
    """Apitoken

     Request API token

    Args:
        username (Any):
        body (BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Token
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    username: Any,
    *,
    client: AuthenticatedClient,
    body: BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset = UNSET,
) -> Response[HTTPValidationError | Token]:
    """Apitoken

     Request API token

    Args:
        username (Any):
        body (BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Token]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: Any,
    *,
    client: AuthenticatedClient,
    body: BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset = UNSET,
) -> HTTPValidationError | Token | None:
    """Apitoken

     Request API token

    Args:
        username (Any):
        body (BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Token
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
        )
    ).parsed
