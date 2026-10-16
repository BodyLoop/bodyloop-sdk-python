from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.report import Report
from ...models.report_update import ReportUpdate
from ...types import Response


def _get_kwargs(
    report_id: int,
    *,
    body: ReportUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/reports/{report_id}".format(
            report_id=quote(str(report_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Report | None:
    if response.status_code == 200:
        response_200 = Report.from_dict(response.json())

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
) -> Response[HTTPValidationError | Report]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    report_id: int,
    *,
    client: AuthenticatedClient,
    body: ReportUpdate,
) -> Response[HTTPValidationError | Report]:
    """Update Report

     Update a report (CR**U**D). Only fields present in the body are changed, the report file is not
    touched.

    **viatars**   Replaces the linked viatars.

    **probands**  Replaces the linked probands.

    Args:
        report_id (int):
        body (ReportUpdate): Updatable fields of a report (PATCH). Only fields present in the
            request are changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Report]
    """

    kwargs = _get_kwargs(
        report_id=report_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    report_id: int,
    *,
    client: AuthenticatedClient,
    body: ReportUpdate,
) -> HTTPValidationError | Report | None:
    """Update Report

     Update a report (CR**U**D). Only fields present in the body are changed, the report file is not
    touched.

    **viatars**   Replaces the linked viatars.

    **probands**  Replaces the linked probands.

    Args:
        report_id (int):
        body (ReportUpdate): Updatable fields of a report (PATCH). Only fields present in the
            request are changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Report
    """

    return sync_detailed(
        report_id=report_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    report_id: int,
    *,
    client: AuthenticatedClient,
    body: ReportUpdate,
) -> Response[HTTPValidationError | Report]:
    """Update Report

     Update a report (CR**U**D). Only fields present in the body are changed, the report file is not
    touched.

    **viatars**   Replaces the linked viatars.

    **probands**  Replaces the linked probands.

    Args:
        report_id (int):
        body (ReportUpdate): Updatable fields of a report (PATCH). Only fields present in the
            request are changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Report]
    """

    kwargs = _get_kwargs(
        report_id=report_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    report_id: int,
    *,
    client: AuthenticatedClient,
    body: ReportUpdate,
) -> HTTPValidationError | Report | None:
    """Update Report

     Update a report (CR**U**D). Only fields present in the body are changed, the report file is not
    touched.

    **viatars**   Replaces the linked viatars.

    **probands**  Replaces the linked probands.

    Args:
        report_id (int):
        body (ReportUpdate): Updatable fields of a report (PATCH). Only fields present in the
            request are changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Report
    """

    return (
        await asyncio_detailed(
            report_id=report_id,
            client=client,
            body=body,
        )
    ).parsed
