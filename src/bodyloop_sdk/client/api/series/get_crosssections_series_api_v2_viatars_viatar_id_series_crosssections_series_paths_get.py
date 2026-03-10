from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    series_paths: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/viatars/{viatar_id}/series/crosssections/{series_paths}".format(
            viatar_id=quote(str(viatar_id), safe=""),
            series_paths=quote(str(series_paths), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[Any] | None:
    if response.status_code == 200:
        response_200 = cast(list[Any], response.json())

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
) -> Response[HTTPValidationError | list[Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    series_paths: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | list[Any]]:
    """Get Crosssections Series

     Returns the crosssection series of the matching viatar and series_paths

    Args:
        viatar_id (int):
        series_paths (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[Any]]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        series_paths=series_paths,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    series_paths: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | list[Any] | None:
    """Get Crosssections Series

     Returns the crosssection series of the matching viatar and series_paths

    Args:
        viatar_id (int):
        series_paths (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[Any]
    """

    return sync_detailed(
        viatar_id=viatar_id,
        series_paths=series_paths,
        client=client,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    series_paths: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | list[Any]]:
    """Get Crosssections Series

     Returns the crosssection series of the matching viatar and series_paths

    Args:
        viatar_id (int):
        series_paths (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[Any]]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        series_paths=series_paths,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    series_paths: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | list[Any] | None:
    """Get Crosssections Series

     Returns the crosssection series of the matching viatar and series_paths

    Args:
        viatar_id (int):
        series_paths (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[Any]
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            series_paths=series_paths,
            client=client,
        )
    ).parsed
