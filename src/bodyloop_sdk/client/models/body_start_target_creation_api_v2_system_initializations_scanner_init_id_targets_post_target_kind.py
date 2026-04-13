from typing import Literal, cast

BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind = Literal["discover", "init"]

BODY_START_TARGET_CREATION_API_V2_SYSTEM_INITIALIZATIONS_SCANNER_INIT_ID_TARGETS_POST_TARGET_KIND_VALUES: set[
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind
] = {
    "discover",
    "init",
}


def check_body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_target_kind(
    value: str,
) -> BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind:
    if (
        value
        in BODY_START_TARGET_CREATION_API_V2_SYSTEM_INITIALIZATIONS_SCANNER_INIT_ID_TARGETS_POST_TARGET_KIND_VALUES
    ):
        return cast(BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_START_TARGET_CREATION_API_V2_SYSTEM_INITIALIZATIONS_SCANNER_INIT_ID_TARGETS_POST_TARGET_KIND_VALUES!r}"
    )
