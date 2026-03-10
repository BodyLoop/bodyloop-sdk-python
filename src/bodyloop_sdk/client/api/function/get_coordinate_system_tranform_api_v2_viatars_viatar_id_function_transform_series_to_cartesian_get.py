from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    viatar_id: int,
    *,
    series_path: str,
    distance_from_root: float,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["series_path"] = series_path

    params["distanceFromRoot"] = distance_from_root

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/viatars/{viatar_id}/function/transform_series_to_cartesian".format(
            viatar_id=quote(str(viatar_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
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
    series_path: str,
    distance_from_root: float,
) -> Response[Any | HTTPValidationError]:
    """Get Coordinate System Tranform

     Convert coordinates form 'series' system into cartesian system

    Args:
        viatar_id (int):
        series_path (str):
        distance_from_root (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        series_path=series_path,
        distance_from_root=distance_from_root,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    series_path: str,
    distance_from_root: float,
) -> Any | HTTPValidationError | None:
    """Get Coordinate System Tranform

     Convert coordinates form 'series' system into cartesian system

    Args:
        viatar_id (int):
        series_path (str):
        distance_from_root (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        viatar_id=viatar_id,
        client=client,
        series_path=series_path,
        distance_from_root=distance_from_root,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    series_path: str,
    distance_from_root: float,
) -> Response[Any | HTTPValidationError]:
    """Get Coordinate System Tranform

     Convert coordinates form 'series' system into cartesian system

    Args:
        viatar_id (int):
        series_path (str):
        distance_from_root (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        series_path=series_path,
        distance_from_root=distance_from_root,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    series_path: str,
    distance_from_root: float,
) -> Any | HTTPValidationError | None:
    """Get Coordinate System Tranform

     Convert coordinates form 'series' system into cartesian system

    Args:
        viatar_id (int):
        series_path (str):
        distance_from_root (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            client=client,
            series_path=series_path,
            distance_from_root=distance_from_root,
        )
    ).parsed
