from typing import Literal

GetEventCountApiV2StatisticCountGetEventStatusType0 = Literal["failure", "success"]

GET_EVENT_COUNT_API_V2_STATISTIC_COUNT_GET_EVENT_STATUS_TYPE_0_VALUES: set[
    GetEventCountApiV2StatisticCountGetEventStatusType0
] = {
    "failure",
    "success",
}


def check_get_event_count_api_v2_statistic_count_get_event_status_type_0(
    value: str,
) -> GetEventCountApiV2StatisticCountGetEventStatusType0:
    if value in GET_EVENT_COUNT_API_V2_STATISTIC_COUNT_GET_EVENT_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EVENT_COUNT_API_V2_STATISTIC_COUNT_GET_EVENT_STATUS_TYPE_0_VALUES!r}"
    )
