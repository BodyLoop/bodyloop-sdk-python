from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.preference import Preference
from ...models.preference_data import PreferenceData
from ...types import Response


def _get_kwargs(
    username: str,
    key: str,
    *,
    body: PreferenceData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/authentification/users/{username}/preferences/{key}".format(
            username=quote(str(username), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Preference | None:
    if response.status_code == 200:
        response_200 = Preference.from_dict(response.json())

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
) -> Response[HTTPValidationError | Preference]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    key: str,
    *,
    client: AuthenticatedClient,
    body: PreferenceData,
) -> Response[HTTPValidationError | Preference]:
    """Update Preference

     Update a preference of a user (CR**U**D)

    Args:
        username (str):
        key (str):
        body (PreferenceData): The flexible value of a preference

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Preference]
    """

    kwargs = _get_kwargs(
        username=username,
        key=key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    key: str,
    *,
    client: AuthenticatedClient,
    body: PreferenceData,
) -> HTTPValidationError | Preference | None:
    """Update Preference

     Update a preference of a user (CR**U**D)

    Args:
        username (str):
        key (str):
        body (PreferenceData): The flexible value of a preference

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Preference
    """

    return sync_detailed(
        username=username,
        key=key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    username: str,
    key: str,
    *,
    client: AuthenticatedClient,
    body: PreferenceData,
) -> Response[HTTPValidationError | Preference]:
    """Update Preference

     Update a preference of a user (CR**U**D)

    Args:
        username (str):
        key (str):
        body (PreferenceData): The flexible value of a preference

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Preference]
    """

    kwargs = _get_kwargs(
        username=username,
        key=key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    key: str,
    *,
    client: AuthenticatedClient,
    body: PreferenceData,
) -> HTTPValidationError | Preference | None:
    """Update Preference

     Update a preference of a user (CR**U**D)

    Args:
        username (str):
        key (str):
        body (PreferenceData): The flexible value of a preference

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Preference
    """

    return (
        await asyncio_detailed(
            username=username,
            key=key,
            client=client,
            body=body,
        )
    ).parsed
