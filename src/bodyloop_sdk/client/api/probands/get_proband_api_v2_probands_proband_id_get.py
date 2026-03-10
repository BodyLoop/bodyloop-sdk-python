from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.proband_detail import ProbandDetail
from ...types import Response


def _get_kwargs(
    proband_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/probands/{proband_id}".format(
            proband_id=quote(str(proband_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ProbandDetail | None:
    if response.status_code == 200:
        response_200 = ProbandDetail.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProbandDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proband_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ProbandDetail]:
    """Get Proband

     Read a proband (C**R**UD)
    The response contains proband data and related viatars.

    Args:
        proband_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProbandDetail]
    """

    kwargs = _get_kwargs(
        proband_id=proband_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proband_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | ProbandDetail | None:
    """Get Proband

     Read a proband (C**R**UD)
    The response contains proband data and related viatars.

    Args:
        proband_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProbandDetail
    """

    return sync_detailed(
        proband_id=proband_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    proband_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ProbandDetail]:
    """Get Proband

     Read a proband (C**R**UD)
    The response contains proband data and related viatars.

    Args:
        proband_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProbandDetail]
    """

    kwargs = _get_kwargs(
        proband_id=proband_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proband_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | ProbandDetail | None:
    """Get Proband

     Read a proband (C**R**UD)
    The response contains proband data and related viatars.

    Args:
        proband_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProbandDetail
    """

    return (
        await asyncio_detailed(
            proband_id=proband_id,
            client=client,
        )
    ).parsed
