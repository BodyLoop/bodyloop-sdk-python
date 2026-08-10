from typing import Literal

ExportOptionsViewFormatType0 = Literal["glb", "obj", "ply", "stl"]

EXPORT_OPTIONS_VIEW_FORMAT_TYPE_0_VALUES: set[ExportOptionsViewFormatType0] = {
    "glb",
    "obj",
    "ply",
    "stl",
}


def check_export_options_view_format_type_0(value: str) -> ExportOptionsViewFormatType0:
    if value in EXPORT_OPTIONS_VIEW_FORMAT_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPORT_OPTIONS_VIEW_FORMAT_TYPE_0_VALUES!r}")
