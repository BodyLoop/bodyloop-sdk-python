from typing import Literal, cast

BiomechSystemManagerModelsViatarTargetStateStatusType0 = Literal[
    "Aborted", "Deleted", "Failed", "Generating", "Pending", "Preparing", "Ready"
]

BIOMECH_SYSTEM_MANAGER_MODELS_VIATAR_TARGET_STATE_STATUS_TYPE_0_VALUES: set[
    BiomechSystemManagerModelsViatarTargetStateStatusType0
] = {
    "Aborted",
    "Deleted",
    "Failed",
    "Generating",
    "Pending",
    "Preparing",
    "Ready",
}


def check_biomech_system_manager_models_viatar_target_state_status_type_0(
    value: str,
) -> BiomechSystemManagerModelsViatarTargetStateStatusType0:
    if value in BIOMECH_SYSTEM_MANAGER_MODELS_VIATAR_TARGET_STATE_STATUS_TYPE_0_VALUES:
        return cast(BiomechSystemManagerModelsViatarTargetStateStatusType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BIOMECH_SYSTEM_MANAGER_MODELS_VIATAR_TARGET_STATE_STATUS_TYPE_0_VALUES!r}"
    )
