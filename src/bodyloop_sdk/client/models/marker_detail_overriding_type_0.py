from typing import Literal, cast

MarkerDetailOverridingType0 = Literal["AutoMarker", "CustomMarker", "PalpationMarker"]

MARKER_DETAIL_OVERRIDING_TYPE_0_VALUES: set[MarkerDetailOverridingType0] = {
    "AutoMarker",
    "CustomMarker",
    "PalpationMarker",
}


def check_marker_detail_overriding_type_0(value: str) -> MarkerDetailOverridingType0:
    if value in MARKER_DETAIL_OVERRIDING_TYPE_0_VALUES:
        return cast(MarkerDetailOverridingType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MARKER_DETAIL_OVERRIDING_TYPE_0_VALUES!r}")
