from typing import Literal

PolygonalChainDetailPreferenceType0 = Literal[
    "geodesic", "linear", "linear_x", "linear_y", "linear_z", "tape_surface", "tape_taut"
]

POLYGONAL_CHAIN_DETAIL_PREFERENCE_TYPE_0_VALUES: set[PolygonalChainDetailPreferenceType0] = {
    "geodesic",
    "linear",
    "linear_x",
    "linear_y",
    "linear_z",
    "tape_surface",
    "tape_taut",
}


def check_polygonal_chain_detail_preference_type_0(value: str) -> PolygonalChainDetailPreferenceType0:
    if value in POLYGONAL_CHAIN_DETAIL_PREFERENCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLYGONAL_CHAIN_DETAIL_PREFERENCE_TYPE_0_VALUES!r}")
