from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_preset_api_v2_presets_post import BodyCreatePresetApiV2PresetsPost
from ...models.http_validation_error import HTTPValidationError
from ...models.preset import Preset
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreatePresetApiV2PresetsPost | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/presets/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Preset | None:
    if response.status_code == 201:
        response_201 = Preset.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: BodyCreatePresetApiV2PresetsPost | Unset = UNSET,
) -> Response[HTTPValidationError | Preset]:
    """Create Preset

     Create a preset (**C**RUD)

    Args:
        body (BodyCreatePresetApiV2PresetsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Preset]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyCreatePresetApiV2PresetsPost | Unset = UNSET,
) -> HTTPValidationError | Preset | None:
    """Create Preset

     Create a preset (**C**RUD)

    Args:
        body (BodyCreatePresetApiV2PresetsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Preset
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreatePresetApiV2PresetsPost | Unset = UNSET,
) -> Response[HTTPValidationError | Preset]:
    """Create Preset

     Create a preset (**C**RUD)

    Args:
        body (BodyCreatePresetApiV2PresetsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Preset]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreatePresetApiV2PresetsPost | Unset = UNSET,
) -> HTTPValidationError | Preset | None:
    """Create Preset

     Create a preset (**C**RUD)

    Args:
        body (BodyCreatePresetApiV2PresetsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Preset
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
