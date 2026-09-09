import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_count_api_v2_statistic_count_get_event_status_type_0 import (
    GetEventCountApiV2StatisticCountGetEventStatusType0,
)
from ...models.get_event_count_api_v2_statistic_count_get_response_get_event_count_api_v2_statistic_count_get import (
    GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    event: None | str | Unset = UNSET,
    event_status: GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset = UNSET,
    info: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start: None | str | Unset
    if isinstance(start, Unset):
        json_start = UNSET
    elif isinstance(start, datetime.datetime):
        json_start = start.isoformat()
    else:
        json_start = start
    params["start"] = json_start

    json_end: None | str | Unset
    if isinstance(end, Unset):
        json_end = UNSET
    elif isinstance(end, datetime.datetime):
        json_end = end.isoformat()
    else:
        json_end = end
    params["end"] = json_end

    json_event: None | str | Unset
    if isinstance(event, Unset):
        json_event = UNSET
    else:
        json_event = event
    params["event"] = json_event

    json_event_status: None | str | Unset
    if isinstance(event_status, Unset):
        json_event_status = UNSET
    elif isinstance(event_status, str):
        json_event_status = event_status
    else:
        json_event_status = event_status
    params["event_status"] = json_event_status

    json_info: None | str | Unset
    if isinstance(info, Unset):
        json_info = UNSET
    else:
        json_info = info
    params["info"] = json_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/statistic/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet.from_dict(
            response.json()
        )

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
) -> Response[GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    event: None | str | Unset = UNSET,
    event_status: GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset = UNSET,
    info: None | str | Unset = UNSET,
) -> Response[GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError]:
    """Get Event Count

     Returns counts for all events, broken down by event, by event & status, and by event & status &
    info.
    `start`/`end` (i.e. 2026-01-01) add a `custom` window counting occurrences within that (inclusive)
    range.
    `event`/`event_status`/`info` are all optional and, when given, restrict the results to that value.

    Args:
        start (datetime.datetime | None | Unset):
        end (datetime.datetime | None | Unset):
        event (None | str | Unset):
        event_status (GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset):
        info (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        event=event,
        event_status=event_status,
        info=info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    event: None | str | Unset = UNSET,
    event_status: GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset = UNSET,
    info: None | str | Unset = UNSET,
) -> GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError | None:
    """Get Event Count

     Returns counts for all events, broken down by event, by event & status, and by event & status &
    info.
    `start`/`end` (i.e. 2026-01-01) add a `custom` window counting occurrences within that (inclusive)
    range.
    `event`/`event_status`/`info` are all optional and, when given, restrict the results to that value.

    Args:
        start (datetime.datetime | None | Unset):
        end (datetime.datetime | None | Unset):
        event (None | str | Unset):
        event_status (GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset):
        info (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        event=event,
        event_status=event_status,
        info=info,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    event: None | str | Unset = UNSET,
    event_status: GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset = UNSET,
    info: None | str | Unset = UNSET,
) -> Response[GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError]:
    """Get Event Count

     Returns counts for all events, broken down by event, by event & status, and by event & status &
    info.
    `start`/`end` (i.e. 2026-01-01) add a `custom` window counting occurrences within that (inclusive)
    range.
    `event`/`event_status`/`info` are all optional and, when given, restrict the results to that value.

    Args:
        start (datetime.datetime | None | Unset):
        end (datetime.datetime | None | Unset):
        event (None | str | Unset):
        event_status (GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset):
        info (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        event=event,
        event_status=event_status,
        info=info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    event: None | str | Unset = UNSET,
    event_status: GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset = UNSET,
    info: None | str | Unset = UNSET,
) -> GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError | None:
    """Get Event Count

     Returns counts for all events, broken down by event, by event & status, and by event & status &
    info.
    `start`/`end` (i.e. 2026-01-01) add a `custom` window counting occurrences within that (inclusive)
    range.
    `event`/`event_status`/`info` are all optional and, when given, restrict the results to that value.

    Args:
        start (datetime.datetime | None | Unset):
        end (datetime.datetime | None | Unset):
        event (None | str | Unset):
        event_status (GetEventCountApiV2StatisticCountGetEventStatusType0 | None | Unset):
        info (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            event=event,
            event_status=event_status,
            info=info,
        )
    ).parsed
