from typing import Literal

AnglePreferenceType0 = Literal["conjugate", "primary", "supplementary"]

ANGLE_PREFERENCE_TYPE_0_VALUES: set[AnglePreferenceType0] = {
    "conjugate",
    "primary",
    "supplementary",
}


def check_angle_preference_type_0(value: str) -> AnglePreferenceType0:
    if value in ANGLE_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANGLE_PREFERENCE_TYPE_0_VALUES!r}")
