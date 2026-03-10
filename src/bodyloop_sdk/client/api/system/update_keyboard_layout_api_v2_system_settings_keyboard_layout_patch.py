from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_keyboard_layout_api_v2_system_settings_keyboard_layout_patch import (
    BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/settings/keyboard_layout",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Update Keyboard Layout

     Update keyboard settings

    Args:
        body (BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    client: AuthenticatedClient | Client,
    body: BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Update Keyboard Layout

     Update keyboard settings

    Args:
        body (BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Update Keyboard Layout

     Update keyboard settings

    Args:
        body (BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Update Keyboard Layout

     Update keyboard settings

    Args:
        body (BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
