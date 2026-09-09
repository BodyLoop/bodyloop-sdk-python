from typing import Literal

AngleDetailPreferenceType0 = Literal["conjugate", "primary", "supplementary"]

ANGLE_DETAIL_PREFERENCE_TYPE_0_VALUES: set[AngleDetailPreferenceType0] = {
    "conjugate",
    "primary",
    "supplementary",
}


def check_angle_detail_preference_type_0(value: str) -> AngleDetailPreferenceType0:
    if value in ANGLE_DETAIL_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANGLE_DETAIL_PREFERENCE_TYPE_0_VALUES!r}")
