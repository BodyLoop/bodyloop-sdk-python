from typing import Literal

BodySetEventApiV2StatisticEventPostEventStatusType0 = Literal["failure", "success"]

BODY_SET_EVENT_API_V2_STATISTIC_EVENT_POST_EVENT_STATUS_TYPE_0_VALUES: set[
    BodySetEventApiV2StatisticEventPostEventStatusType0
] = {
    "failure",
    "success",
}


def check_body_set_event_api_v2_statistic_event_post_event_status_type_0(
    value: str,
) -> BodySetEventApiV2StatisticEventPostEventStatusType0:
    if value in BODY_SET_EVENT_API_V2_STATISTIC_EVENT_POST_EVENT_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_SET_EVENT_API_V2_STATISTIC_EVENT_POST_EVENT_STATUS_TYPE_0_VALUES!r}"
    )
