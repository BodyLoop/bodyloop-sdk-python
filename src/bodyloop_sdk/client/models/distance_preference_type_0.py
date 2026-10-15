from typing import Literal

DistancePreferenceType0 = Literal["geodesic", "linear", "linear_x", "linear_y", "linear_z", "tape_surface", "tape_taut"]

DISTANCE_PREFERENCE_TYPE_0_VALUES: set[DistancePreferenceType0] = {
    "geodesic",
    "linear",
    "linear_x",
    "linear_y",
    "linear_z",
    "tape_surface",
    "tape_taut",
}


def check_distance_preference_type_0(value: str) -> DistancePreferenceType0:
    if value in DISTANCE_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DISTANCE_PREFERENCE_TYPE_0_VALUES!r}")
