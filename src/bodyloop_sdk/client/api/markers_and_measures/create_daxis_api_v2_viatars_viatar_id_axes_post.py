from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.axis import Axis
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    *,
    body: Axis,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/viatars/{viatar_id}/axes/".format(
            viatar_id=quote(str(viatar_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = response.json()
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
    body: Axis,
) -> Response[Any | HTTPValidationError]:
    """Create Daxis

    Args:
        viatar_id (int):
        body (Axis): Axis representation through two markers Example: {'axis_path':
            'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive label',
            'markers': ['marker_a', 'marker_b'], 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: Axis,
) -> Any | HTTPValidationError | None:
    """Create Daxis

    Args:
        viatar_id (int):
        body (Axis): Axis representation through two markers Example: {'axis_path':
            'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive label',
            'markers': ['marker_a', 'marker_b'], 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        viatar_id=viatar_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: Axis,
) -> Response[Any | HTTPValidationError]:
    """Create Daxis

    Args:
        viatar_id (int):
        body (Axis): Axis representation through two markers Example: {'axis_path':
            'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive label',
            'markers': ['marker_a', 'marker_b'], 'note': 'Meaningful description...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: Axis,
) -> Any | HTTPValidationError | None:
    """Create Daxis

    Args:
        viatar_id (int):
        body (Axis): Axis representation through two markers Example: {'axis_path':
            'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive label',
            'markers': ['marker_a', 'marker_b'], 'note': 'Meaningful description...'}.

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
            body=body,
        )
    ).parsed
