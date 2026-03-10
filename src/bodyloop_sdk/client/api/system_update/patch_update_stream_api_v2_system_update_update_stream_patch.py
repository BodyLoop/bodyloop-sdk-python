from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_patch_update_stream_api_v2_system_update_update_stream_patch import (
    BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/update/update_stream",
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
    client: AuthenticatedClient,
    body: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Patch Update Stream

     Patch update stream

    Args:
        body (BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset):

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
    client: AuthenticatedClient,
    body: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Patch Update Stream

     Patch update stream

    Args:
        body (BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset):

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
    client: AuthenticatedClient,
    body: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Patch Update Stream

     Patch update stream

    Args:
        body (BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset):

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
    client: AuthenticatedClient,
    body: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Patch Update Stream

     Patch update stream

    Args:
        body (BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch | Unset):

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
