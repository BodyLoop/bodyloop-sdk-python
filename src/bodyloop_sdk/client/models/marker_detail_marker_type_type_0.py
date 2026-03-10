from typing import Literal, cast

MarkerDetailMarkerTypeType0 = Literal["AutoMarker", "CustomMarker", "PalpationMarker"]

MARKER_DETAIL_MARKER_TYPE_TYPE_0_VALUES: set[MarkerDetailMarkerTypeType0] = {
    "AutoMarker",
    "CustomMarker",
    "PalpationMarker",
}


def check_marker_detail_marker_type_type_0(value: str) -> MarkerDetailMarkerTypeType0:
    if value in MARKER_DETAIL_MARKER_TYPE_TYPE_0_VALUES:
        return cast(MarkerDetailMarkerTypeType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MARKER_DETAIL_MARKER_TYPE_TYPE_0_VALUES!r}")
