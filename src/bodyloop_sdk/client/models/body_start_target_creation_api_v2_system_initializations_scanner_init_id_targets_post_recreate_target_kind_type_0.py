from typing import Literal

BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0 = Literal[
    "discover", "init"
]

BODY_START_TARGET_CREATION_API_V2_SYSTEM_INITIALIZATIONS_SCANNER_INIT_ID_TARGETS_POST_RECREATE_TARGET_KIND_TYPE_0_VALUES: set[
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0
] = {
    "discover",
    "init",
}


def check_body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_recreate_target_kind_type_0(
    value: str,
) -> BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0:
    if (
        value
        in BODY_START_TARGET_CREATION_API_V2_SYSTEM_INITIALIZATIONS_SCANNER_INIT_ID_TARGETS_POST_RECREATE_TARGET_KIND_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_START_TARGET_CREATION_API_V2_SYSTEM_INITIALIZATIONS_SCANNER_INIT_ID_TARGETS_POST_RECREATE_TARGET_KIND_TYPE_0_VALUES!r}"
    )
