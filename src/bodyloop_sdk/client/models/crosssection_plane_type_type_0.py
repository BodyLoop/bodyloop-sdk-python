from typing import Literal

CrosssectionPlaneTypeType0 = Literal["markers", "normal", "skeleton"]

CROSSSECTION_PLANE_TYPE_TYPE_0_VALUES: set[CrosssectionPlaneTypeType0] = {
    "markers",
    "normal",
    "skeleton",
}


def check_crosssection_plane_type_type_0(value: str) -> CrosssectionPlaneTypeType0:
    if value in CROSSSECTION_PLANE_TYPE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CROSSSECTION_PLANE_TYPE_TYPE_0_VALUES!r}")
