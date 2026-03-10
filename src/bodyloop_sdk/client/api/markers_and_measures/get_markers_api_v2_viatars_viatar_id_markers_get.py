from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.marker_detail import MarkerDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    viatar_id: int,
    *,
    marker_type: Any | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["marker_type"] = marker_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/viatars/{viatar_id}/markers/".format(
            viatar_id=quote(str(viatar_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[MarkerDetail] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MarkerDetail.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[MarkerDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    marker_type: Any | Unset = UNSET,
) -> Response[HTTPValidationError | list[MarkerDetail]]:
    """Get Markers

    Args:
        viatar_id (int):
        marker_type (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[MarkerDetail]]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        marker_type=marker_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    marker_type: Any | Unset = UNSET,
) -> HTTPValidationError | list[MarkerDetail] | None:
    """Get Markers

    Args:
        viatar_id (int):
        marker_type (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[MarkerDetail]
    """

    return sync_detailed(
        viatar_id=viatar_id,
        client=client,
        marker_type=marker_type,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    marker_type: Any | Unset = UNSET,
) -> Response[HTTPValidationError | list[MarkerDetail]]:
    """Get Markers

    Args:
        viatar_id (int):
        marker_type (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[MarkerDetail]]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        marker_type=marker_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    marker_type: Any | Unset = UNSET,
) -> HTTPValidationError | list[MarkerDetail] | None:
    """Get Markers

    Args:
        viatar_id (int):
        marker_type (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[MarkerDetail]
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            client=client,
            marker_type=marker_type,
        )
    ).parsed
