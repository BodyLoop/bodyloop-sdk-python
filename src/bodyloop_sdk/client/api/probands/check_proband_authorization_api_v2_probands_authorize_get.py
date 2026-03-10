from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.proband import Proband
from ...types import UNSET, Response


def _get_kwargs(
    *,
    proband_code: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["proband_code"] = proband_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/probands/authorize",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Proband | None:
    if response.status_code == 200:
        response_200 = Proband.from_dict(response.json())

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
    proband_code: str,
) -> Response[HTTPValidationError | Proband]:
    """Check Proband Authorization

    Args:
        proband_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Proband]
    """

    kwargs = _get_kwargs(
        proband_code=proband_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    proband_code: str,
) -> HTTPValidationError | Proband | None:
    """Check Proband Authorization

    Args:
        proband_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Proband
    """

    return sync_detailed(
        client=client,
        proband_code=proband_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    proband_code: str,
) -> Response[HTTPValidationError | Proband]:
    """Check Proband Authorization

    Args:
        proband_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Proband]
    """

    kwargs = _get_kwargs(
        proband_code=proband_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    proband_code: str,
) -> HTTPValidationError | Proband | None:
    """Check Proband Authorization

    Args:
        proband_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Proband
    """

    return (
        await asyncio_detailed(
            client=client,
            proband_code=proband_code,
        )
    ).parsed
