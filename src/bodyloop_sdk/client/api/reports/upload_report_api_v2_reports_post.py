from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_report_api_v2_reports_post import BodyUploadReportApiV2ReportsPost
from ...models.http_validation_error import HTTPValidationError
from ...models.report import Report
from ...types import Response


def _get_kwargs(
    *,
    body: BodyUploadReportApiV2ReportsPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/reports",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Report | None:
    if response.status_code == 201:
        response_201 = Report.from_dict(response.json())

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
) -> Response[HTTPValidationError | Report]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadReportApiV2ReportsPost,
) -> Response[HTTPValidationError | Report]:
    """Upload Report

     Upload a pdf as report (**C**RUD)

    **file**          The report as pdf file.

    **viatars**       Ids of the viatars the report belongs to.

    **probands**      Ids of the probands the report belongs to (empty: linked to no viatar/proband).

    **label**         Optional label of the report.

    **note**          Optional note of the report.

    **key_external**  Optional key of the report in an external system.

    Args:
        body (BodyUploadReportApiV2ReportsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Report]
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
    body: BodyUploadReportApiV2ReportsPost,
) -> HTTPValidationError | Report | None:
    """Upload Report

     Upload a pdf as report (**C**RUD)

    **file**          The report as pdf file.

    **viatars**       Ids of the viatars the report belongs to.

    **probands**      Ids of the probands the report belongs to (empty: linked to no viatar/proband).

    **label**         Optional label of the report.

    **note**          Optional note of the report.

    **key_external**  Optional key of the report in an external system.

    Args:
        body (BodyUploadReportApiV2ReportsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Report
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadReportApiV2ReportsPost,
) -> Response[HTTPValidationError | Report]:
    """Upload Report

     Upload a pdf as report (**C**RUD)

    **file**          The report as pdf file.

    **viatars**       Ids of the viatars the report belongs to.

    **probands**      Ids of the probands the report belongs to (empty: linked to no viatar/proband).

    **label**         Optional label of the report.

    **note**          Optional note of the report.

    **key_external**  Optional key of the report in an external system.

    Args:
        body (BodyUploadReportApiV2ReportsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Report]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyUploadReportApiV2ReportsPost,
) -> HTTPValidationError | Report | None:
    """Upload Report

     Upload a pdf as report (**C**RUD)

    **file**          The report as pdf file.

    **viatars**       Ids of the viatars the report belongs to.

    **probands**      Ids of the probands the report belongs to (empty: linked to no viatar/proband).

    **label**         Optional label of the report.

    **note**          Optional note of the report.

    **key_external**  Optional key of the report in an external system.

    Args:
        body (BodyUploadReportApiV2ReportsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Report
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
