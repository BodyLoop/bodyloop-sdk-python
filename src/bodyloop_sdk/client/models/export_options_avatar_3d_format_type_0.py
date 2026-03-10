from typing import Literal, cast

ExportOptionsAvatar3DFormatType0 = Literal["glb", "obj", "ply", "stl"]

EXPORT_OPTIONS_AVATAR_3D_FORMAT_TYPE_0_VALUES: set[ExportOptionsAvatar3DFormatType0] = {
    "glb",
    "obj",
    "ply",
    "stl",
}


def check_export_options_avatar_3d_format_type_0(value: str) -> ExportOptionsAvatar3DFormatType0:
    if value in EXPORT_OPTIONS_AVATAR_3D_FORMAT_TYPE_0_VALUES:
        return cast(ExportOptionsAvatar3DFormatType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPORT_OPTIONS_AVATAR_3D_FORMAT_TYPE_0_VALUES!r}")
