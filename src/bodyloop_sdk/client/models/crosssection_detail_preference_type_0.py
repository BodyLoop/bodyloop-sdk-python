from typing import Literal

CrosssectionDetailPreferenceType0 = Literal["convex", "perimeter"]

CROSSSECTION_DETAIL_PREFERENCE_TYPE_0_VALUES: set[CrosssectionDetailPreferenceType0] = {
    "convex",
    "perimeter",
}


def check_crosssection_detail_preference_type_0(value: str) -> CrosssectionDetailPreferenceType0:
    if value in CROSSSECTION_DETAIL_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CROSSSECTION_DETAIL_PREFERENCE_TYPE_0_VALUES!r}")
