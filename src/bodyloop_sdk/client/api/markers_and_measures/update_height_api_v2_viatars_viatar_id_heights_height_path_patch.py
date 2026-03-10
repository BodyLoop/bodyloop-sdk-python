from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.height import Height
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    height_path: str,
    *,
    body: Height,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/viatars/{viatar_id}/heights/{height_path}".format(
            viatar_id=quote(str(viatar_id), safe=""),
            height_path=quote(str(height_path), safe=""),
        ),
    }

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
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
    body: Height,
) -> Response[Any | HTTPValidationError]:
    """Update Height

    Args:
        viatar_id (int):
        height_path (str):
        body (Height): Height representation of one marker Example: {'at_marker': 'marker_a',
            'height_path': 'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive
            label', 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        height_path=height_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
    body: Height,
) -> Any | HTTPValidationError | None:
    """Update Height

    Args:
        viatar_id (int):
        height_path (str):
        body (Height): Height representation of one marker Example: {'at_marker': 'marker_a',
            'height_path': 'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive
            label', 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        viatar_id=viatar_id,
        height_path=height_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
    body: Height,
) -> Response[Any | HTTPValidationError]:
    """Update Height

    Args:
        viatar_id (int):
        height_path (str):
        body (Height): Height representation of one marker Example: {'at_marker': 'marker_a',
            'height_path': 'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive
            label', 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        height_path=height_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    height_path: str,
    *,
    client: AuthenticatedClient,
    body: Height,
) -> Any | HTTPValidationError | None:
    """Update Height

    Args:
        viatar_id (int):
        height_path (str):
        body (Height): Height representation of one marker Example: {'at_marker': 'marker_a',
            'height_path': 'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive
            label', 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            height_path=height_path,
            client=client,
            body=body,
        )
    ).parsed
