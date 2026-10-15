from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.polygonal_chain_detail import PolygonalChainDetail
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    polygonal_chain_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/viatars/{viatar_id}/polygonal_chains/{polygonal_chain_path}".format(
            viatar_id=quote(str(viatar_id), safe=""),
            polygonal_chain_path=quote(str(polygonal_chain_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PolygonalChainDetail | None:
    if response.status_code == 200:
        response_200 = PolygonalChainDetail.from_dict(response.json())

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
) -> Response[HTTPValidationError | PolygonalChainDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    polygonal_chain_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | PolygonalChainDetail]:
    """Get Polygonal Chain

    Args:
        viatar_id (int):
        polygonal_chain_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolygonalChainDetail]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        polygonal_chain_path=polygonal_chain_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    polygonal_chain_path: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | PolygonalChainDetail | None:
    """Get Polygonal Chain

    Args:
        viatar_id (int):
        polygonal_chain_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolygonalChainDetail
    """

    return sync_detailed(
        viatar_id=viatar_id,
        polygonal_chain_path=polygonal_chain_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    polygonal_chain_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | PolygonalChainDetail]:
    """Get Polygonal Chain

    Args:
        viatar_id (int):
        polygonal_chain_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolygonalChainDetail]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        polygonal_chain_path=polygonal_chain_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    polygonal_chain_path: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | PolygonalChainDetail | None:
    """Get Polygonal Chain

    Args:
        viatar_id (int):
        polygonal_chain_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolygonalChainDetail
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            polygonal_chain_path=polygonal_chain_path,
            client=client,
        )
    ).parsed
