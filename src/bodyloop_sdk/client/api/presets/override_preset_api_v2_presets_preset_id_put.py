from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_override_preset_api_v2_presets_preset_id_put import BodyOverridePresetApiV2PresetsPresetIdPut
from ...models.http_validation_error import HTTPValidationError
from ...models.preset import Preset
from ...types import UNSET, Response, Unset


def _get_kwargs(
    preset_id: int,
    *,
    body: BodyOverridePresetApiV2PresetsPresetIdPut | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/presets/{preset_id}".format(
            preset_id=quote(str(preset_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Preset | None:
    if response.status_code == 200:
        response_200 = Preset.from_dict(response.json())

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
) -> Response[HTTPValidationError | Preset]:
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
    body: BodyOverridePresetApiV2PresetsPresetIdPut | Unset = UNSET,
) -> Response[HTTPValidationError | Preset]:
    """Override Preset

     Override a preset (CR**U**D)

    Args:
        preset_id (int):
        body (BodyOverridePresetApiV2PresetsPresetIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Preset]
    """

    kwargs = _get_kwargs(
        preset_id=preset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    preset_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyOverridePresetApiV2PresetsPresetIdPut | Unset = UNSET,
) -> HTTPValidationError | Preset | None:
    """Override Preset

     Override a preset (CR**U**D)

    Args:
        preset_id (int):
        body (BodyOverridePresetApiV2PresetsPresetIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Preset
    """

    return sync_detailed(
        preset_id=preset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    preset_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyOverridePresetApiV2PresetsPresetIdPut | Unset = UNSET,
) -> Response[HTTPValidationError | Preset]:
    """Override Preset

     Override a preset (CR**U**D)

    Args:
        preset_id (int):
        body (BodyOverridePresetApiV2PresetsPresetIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Preset]
    """

    kwargs = _get_kwargs(
        preset_id=preset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    preset_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyOverridePresetApiV2PresetsPresetIdPut | Unset = UNSET,
) -> HTTPValidationError | Preset | None:
    """Override Preset

     Override a preset (CR**U**D)

    Args:
        preset_id (int):
        body (BodyOverridePresetApiV2PresetsPresetIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Preset
    """

    return (
        await asyncio_detailed(
            preset_id=preset_id,
            client=client,
            body=body,
        )
    ).parsed
