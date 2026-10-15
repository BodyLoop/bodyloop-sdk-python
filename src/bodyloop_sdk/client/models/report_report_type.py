from typing import Literal

ReportReportType = Literal["upload", "viatar"]

REPORT_REPORT_TYPE_VALUES: set[ReportReportType] = {
    "upload",
    "viatar",
}


def check_report_report_type(value: str) -> ReportReportType:
    if value in REPORT_REPORT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_REPORT_TYPE_VALUES!r}")
