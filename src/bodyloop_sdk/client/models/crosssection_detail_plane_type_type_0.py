from typing import Literal

CrosssectionDetailPlaneTypeType0 = Literal["markers", "normal", "skeleton"]

CROSSSECTION_DETAIL_PLANE_TYPE_TYPE_0_VALUES: set[CrosssectionDetailPlaneTypeType0] = {
    "markers",
    "normal",
    "skeleton",
}


def check_crosssection_detail_plane_type_type_0(value: str) -> CrosssectionDetailPlaneTypeType0:
    if value in CROSSSECTION_DETAIL_PLANE_TYPE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CROSSSECTION_DETAIL_PLANE_TYPE_TYPE_0_VALUES!r}")
