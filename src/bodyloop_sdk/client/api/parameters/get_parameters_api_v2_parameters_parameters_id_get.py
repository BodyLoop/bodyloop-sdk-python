from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.parameters import Parameters
from ...types import Response


def _get_kwargs(
    parameters_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/parameters/{parameters_id}".format(
            parameters_id=quote(str(parameters_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Parameters | None:
    if response.status_code == 200:
        response_200 = Parameters.from_dict(response.json())

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
) -> Response[HTTPValidationError | Parameters]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parameters_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | Parameters]:
    """Get Parameters

     Read a parameters (C**R**UD)
    The response contains parameters data.

    Args:
        parameters_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Parameters]
    """

    kwargs = _get_kwargs(
        parameters_id=parameters_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    parameters_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | Parameters | None:
    """Get Parameters

     Read a parameters (C**R**UD)
    The response contains parameters data.

    Args:
        parameters_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Parameters
    """

    return sync_detailed(
        parameters_id=parameters_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    parameters_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | Parameters]:
    """Get Parameters

     Read a parameters (C**R**UD)
    The response contains parameters data.

    Args:
        parameters_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Parameters]
    """

    kwargs = _get_kwargs(
        parameters_id=parameters_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    parameters_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | Parameters | None:
    """Get Parameters

     Read a parameters (C**R**UD)
    The response contains parameters data.

    Args:
        parameters_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Parameters
    """

    return (
        await asyncio_detailed(
            parameters_id=parameters_id,
            client=client,
        )
    ).parsed
