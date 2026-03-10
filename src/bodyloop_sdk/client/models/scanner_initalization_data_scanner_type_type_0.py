from typing import Literal, cast

ScannerInitalizationDataScannerTypeType0 = Literal["2pillar_16cam", "4pillar_32cam"]

SCANNER_INITALIZATION_DATA_SCANNER_TYPE_TYPE_0_VALUES: set[ScannerInitalizationDataScannerTypeType0] = {
    "2pillar_16cam",
    "4pillar_32cam",
}


def check_scanner_initalization_data_scanner_type_type_0(value: str) -> ScannerInitalizationDataScannerTypeType0:
    if value in SCANNER_INITALIZATION_DATA_SCANNER_TYPE_TYPE_0_VALUES:
        return cast(ScannerInitalizationDataScannerTypeType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCANNER_INITALIZATION_DATA_SCANNER_TYPE_TYPE_0_VALUES!r}"
    )
