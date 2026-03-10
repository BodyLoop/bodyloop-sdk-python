from typing import Literal, cast

BiomechSystemManagerModelsScannerInitTargetStateStatusType0 = Literal[
    "Aborted", "Failed", "Generating", "Pending", "Preparing", "Ready"
]

BIOMECH_SYSTEM_MANAGER_MODELS_SCANNER_INIT_TARGET_STATE_STATUS_TYPE_0_VALUES: set[
    BiomechSystemManagerModelsScannerInitTargetStateStatusType0
] = {
    "Aborted",
    "Failed",
    "Generating",
    "Pending",
    "Preparing",
    "Ready",
}


def check_biomech_system_manager_models_scanner_init_target_state_status_type_0(
    value: str,
) -> BiomechSystemManagerModelsScannerInitTargetStateStatusType0:
    if value in BIOMECH_SYSTEM_MANAGER_MODELS_SCANNER_INIT_TARGET_STATE_STATUS_TYPE_0_VALUES:
        return cast(BiomechSystemManagerModelsScannerInitTargetStateStatusType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BIOMECH_SYSTEM_MANAGER_MODELS_SCANNER_INIT_TARGET_STATE_STATUS_TYPE_0_VALUES!r}"
    )
