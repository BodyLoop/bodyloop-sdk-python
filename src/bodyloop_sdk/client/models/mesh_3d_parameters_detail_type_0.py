from typing import Literal, cast

Mesh3DParametersDetailType0 = Literal["High", "Normal", "Preview"]

MESH_3D_PARAMETERS_DETAIL_TYPE_0_VALUES: set[Mesh3DParametersDetailType0] = {
    "High",
    "Normal",
    "Preview",
}


def check_mesh_3d_parameters_detail_type_0(value: str) -> Mesh3DParametersDetailType0:
    if value in MESH_3D_PARAMETERS_DETAIL_TYPE_0_VALUES:
        return cast(Mesh3DParametersDetailType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESH_3D_PARAMETERS_DETAIL_TYPE_0_VALUES!r}")
