from typing import Literal, cast

ExportOptionsMesh3DFormatType0 = Literal["glb", "obj", "ply", "stl"]

EXPORT_OPTIONS_MESH_3D_FORMAT_TYPE_0_VALUES: set[ExportOptionsMesh3DFormatType0] = {
    "glb",
    "obj",
    "ply",
    "stl",
}


def check_export_options_mesh_3d_format_type_0(value: str) -> ExportOptionsMesh3DFormatType0:
    if value in EXPORT_OPTIONS_MESH_3D_FORMAT_TYPE_0_VALUES:
        return cast(ExportOptionsMesh3DFormatType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPORT_OPTIONS_MESH_3D_FORMAT_TYPE_0_VALUES!r}")
