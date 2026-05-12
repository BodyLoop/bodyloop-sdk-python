from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_axis_api_v2_viatars_viatar_id_axes_axis_path_delete_response_delete_axis_api_v2_viatars_viatar_id_axes_axis_path_delete import (
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    axis_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/viatars/{viatar_id}/axes/{axis_path}".format(
            viatar_id=quote(str(viatar_id), safe=""),
            axis_path=quote(str(axis_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete.from_dict(
            response.json()
        )

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
) -> Response[
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    axis_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete
    | HTTPValidationError
]:
    """Delete Axis

    Args:
        viatar_id (int):
        axis_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        axis_path=axis_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    axis_path: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete
    | HTTPValidationError
    | None
):
    """Delete Axis

    Args:
        viatar_id (int):
        axis_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete | HTTPValidationError
    """

    return sync_detailed(
        viatar_id=viatar_id,
        axis_path=axis_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    axis_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete
    | HTTPValidationError
]:
    """Delete Axis

    Args:
        viatar_id (int):
        axis_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        axis_path=axis_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    axis_path: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete
    | HTTPValidationError
    | None
):
    """Delete Axis

    Args:
        viatar_id (int):
        axis_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            axis_path=axis_path,
            client=client,
        )
    ).parsed
