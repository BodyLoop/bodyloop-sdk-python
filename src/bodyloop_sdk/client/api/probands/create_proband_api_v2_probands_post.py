from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.proband import Proband
from ...models.proband_data import ProbandData
from ...types import Response


def _get_kwargs(
    *,
    body: ProbandData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/probands/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Proband | None:
    if response.status_code == 201:
        response_201 = Proband.from_dict(response.json())

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
) -> Response[HTTPValidationError | Proband]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProbandData,
) -> Response[HTTPValidationError | Proband]:
    """Create Proband

     Create a proband (**C**RUD)

    Args:
        body (ProbandData): Summary of ProbandData Example: {'address': {'city': 'Stuttgart',
            'country': 'Germany', 'street': 'Hauptstraße 20', 'zip_code': '70173'}, 'contact':
            {'email': 'sophie.neumann@example.de', 'phone': '+49-711-12345678'}, 'date_of_birth':
            '1994-06-18', 'gender': 'female', 'key_external': 'ATH11223', 'name_family': 'Neumann',
            'name_given': 'Sophie', 'note': 'Früherer Kreuzbandriss'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Proband]
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
    body: ProbandData,
) -> HTTPValidationError | Proband | None:
    """Create Proband

     Create a proband (**C**RUD)

    Args:
        body (ProbandData): Summary of ProbandData Example: {'address': {'city': 'Stuttgart',
            'country': 'Germany', 'street': 'Hauptstraße 20', 'zip_code': '70173'}, 'contact':
            {'email': 'sophie.neumann@example.de', 'phone': '+49-711-12345678'}, 'date_of_birth':
            '1994-06-18', 'gender': 'female', 'key_external': 'ATH11223', 'name_family': 'Neumann',
            'name_given': 'Sophie', 'note': 'Früherer Kreuzbandriss'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Proband
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProbandData,
) -> Response[HTTPValidationError | Proband]:
    """Create Proband

     Create a proband (**C**RUD)

    Args:
        body (ProbandData): Summary of ProbandData Example: {'address': {'city': 'Stuttgart',
            'country': 'Germany', 'street': 'Hauptstraße 20', 'zip_code': '70173'}, 'contact':
            {'email': 'sophie.neumann@example.de', 'phone': '+49-711-12345678'}, 'date_of_birth':
            '1994-06-18', 'gender': 'female', 'key_external': 'ATH11223', 'name_family': 'Neumann',
            'name_given': 'Sophie', 'note': 'Früherer Kreuzbandriss'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Proband]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProbandData,
) -> HTTPValidationError | Proband | None:
    """Create Proband

     Create a proband (**C**RUD)

    Args:
        body (ProbandData): Summary of ProbandData Example: {'address': {'city': 'Stuttgart',
            'country': 'Germany', 'street': 'Hauptstraße 20', 'zip_code': '70173'}, 'contact':
            {'email': 'sophie.neumann@example.de', 'phone': '+49-711-12345678'}, 'date_of_birth':
            '1994-06-18', 'gender': 'female', 'key_external': 'ATH11223', 'name_family': 'Neumann',
            'name_given': 'Sophie', 'note': 'Früherer Kreuzbandriss'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Proband
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
