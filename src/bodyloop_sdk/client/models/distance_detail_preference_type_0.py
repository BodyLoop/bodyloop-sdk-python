from typing import Literal

DistanceDetailPreferenceType0 = Literal[
    "geodesic", "linear", "linear_x", "linear_y", "linear_z", "tape_surface", "tape_taut"
]

DISTANCE_DETAIL_PREFERENCE_TYPE_0_VALUES: set[DistanceDetailPreferenceType0] = {
    "geodesic",
    "linear",
    "linear_x",
    "linear_y",
    "linear_z",
    "tape_surface",
    "tape_taut",
}


def check_distance_detail_preference_type_0(value: str) -> DistanceDetailPreferenceType0:
    if value in DISTANCE_DETAIL_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DISTANCE_DETAIL_PREFERENCE_TYPE_0_VALUES!r}")
