from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.state import State
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/states",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> State | None:
    if response.status_code == 200:
        response_200 = State.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[State]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[State]:
    """Get Status

     Returns information about the BodyLoop. Inclued hirarchic sub states and combined states.

    **General_State**         A general combined State

    **Backend_State**         Contains information about the Backend (disk_usage)

    **Initialization_State**  Contains information about the system initialization

    **Acquisition_State**     Contains state about the Scan Unit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[State]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> State | None:
    """Get Status

     Returns information about the BodyLoop. Inclued hirarchic sub states and combined states.

    **General_State**         A general combined State

    **Backend_State**         Contains information about the Backend (disk_usage)

    **Initialization_State**  Contains information about the system initialization

    **Acquisition_State**     Contains state about the Scan Unit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        State
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[State]:
    """Get Status

     Returns information about the BodyLoop. Inclued hirarchic sub states and combined states.

    **General_State**         A general combined State

    **Backend_State**         Contains information about the Backend (disk_usage)

    **Initialization_State**  Contains information about the system initialization

    **Acquisition_State**     Contains state about the Scan Unit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[State]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> State | None:
    """Get Status

     Returns information about the BodyLoop. Inclued hirarchic sub states and combined states.

    **General_State**         A general combined State

    **Backend_State**         Contains information about the Backend (disk_usage)

    **Initialization_State**  Contains information about the system initialization

    **Acquisition_State**     Contains state about the Scan Unit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        State
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
