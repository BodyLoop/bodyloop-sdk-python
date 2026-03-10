from typing import Literal, cast

ScannerInitalizationScannerTypeType0 = Literal["2pillar_16cam", "4pillar_32cam"]

SCANNER_INITALIZATION_SCANNER_TYPE_TYPE_0_VALUES: set[ScannerInitalizationScannerTypeType0] = {
    "2pillar_16cam",
    "4pillar_32cam",
}


def check_scanner_initalization_scanner_type_type_0(value: str) -> ScannerInitalizationScannerTypeType0:
    if value in SCANNER_INITALIZATION_SCANNER_TYPE_TYPE_0_VALUES:
        return cast(ScannerInitalizationScannerTypeType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCANNER_INITALIZATION_SCANNER_TYPE_TYPE_0_VALUES!r}")
