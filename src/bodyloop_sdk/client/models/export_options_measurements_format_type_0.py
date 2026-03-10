from typing import Literal, cast

ExportOptionsMeasurementsFormatType0 = Literal["csv", "json"]

EXPORT_OPTIONS_MEASUREMENTS_FORMAT_TYPE_0_VALUES: set[ExportOptionsMeasurementsFormatType0] = {
    "csv",
    "json",
}


def check_export_options_measurements_format_type_0(value: str) -> ExportOptionsMeasurementsFormatType0:
    if value in EXPORT_OPTIONS_MEASUREMENTS_FORMAT_TYPE_0_VALUES:
        return cast(ExportOptionsMeasurementsFormatType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPORT_OPTIONS_MEASUREMENTS_FORMAT_TYPE_0_VALUES!r}")
