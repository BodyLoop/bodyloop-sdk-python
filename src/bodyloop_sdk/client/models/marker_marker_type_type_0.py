from typing import Literal, cast

MarkerMarkerTypeType0 = Literal["AutoMarker", "CustomMarker", "PalpationMarker"]

MARKER_MARKER_TYPE_TYPE_0_VALUES: set[MarkerMarkerTypeType0] = {
    "AutoMarker",
    "CustomMarker",
    "PalpationMarker",
}


def check_marker_marker_type_type_0(value: str) -> MarkerMarkerTypeType0:
    if value in MARKER_MARKER_TYPE_TYPE_0_VALUES:
        return cast(MarkerMarkerTypeType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MARKER_MARKER_TYPE_TYPE_0_VALUES!r}")
