from typing import Literal

CrosssectionPreferenceType0 = Literal["convex", "perimeter"]

CROSSSECTION_PREFERENCE_TYPE_0_VALUES: set[CrosssectionPreferenceType0] = {
    "convex",
    "perimeter",
}


def check_crosssection_preference_type_0(value: str) -> CrosssectionPreferenceType0:
    if value in CROSSSECTION_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CROSSSECTION_PREFERENCE_TYPE_0_VALUES!r}")
