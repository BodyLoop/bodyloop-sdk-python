from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_preset_api_v2_presets_preset_id_delete_response_delete_preset_api_v2_presets_preset_id_delete import (
    DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    preset_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/presets/{preset_id}".format(
            preset_id=quote(str(preset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete.from_dict(
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
    DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    preset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError
]:
    """Delete Preset

     Delete a preset (CRU**D**)

    Args:
        preset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        preset_id=preset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    preset_id: int,
    *,
    client: AuthenticatedClient,
) -> DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError | None:
    """Delete Preset

     Delete a preset (CRU**D**)

    Args:
        preset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError
    """

    return sync_detailed(
        preset_id=preset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    preset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError
]:
    """Delete Preset

     Delete a preset (CRU**D**)

    Args:
        preset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        preset_id=preset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    preset_id: int,
    *,
    client: AuthenticatedClient,
) -> DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError | None:
    """Delete Preset

     Delete a preset (CRU**D**)

    Args:
        preset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            preset_id=preset_id,
            client=client,
        )
    ).parsed
