from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.height_detail import HeightDetail
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    height_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/viatars/{viatar_id}/heights/{height_path}".format(
            viatar_id=quote(str(viatar_id), safe=""),
            height_path=quote(str(height_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | HeightDetail | None:
    if response.status_code == 200:
        response_200 = HeightDetail.from_dict(response.json())

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
) -> Response[HTTPValidationError | HeightDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | HeightDetail]:
    """Get Height

    Args:
        viatar_id (int):
        height_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | HeightDetail]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        height_path=height_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | HeightDetail | None:
    """Get Height

    Args:
        viatar_id (int):
        height_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | HeightDetail
    """

    return sync_detailed(
        viatar_id=viatar_id,
        height_path=height_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | HeightDetail]:
    """Get Height

    Args:
        viatar_id (int):
        height_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | HeightDetail]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        height_path=height_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | HeightDetail | None:
    """Get Height

    Args:
        viatar_id (int):
        height_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | HeightDetail
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            height_path=height_path,
            client=client,
        )
    ).parsed
