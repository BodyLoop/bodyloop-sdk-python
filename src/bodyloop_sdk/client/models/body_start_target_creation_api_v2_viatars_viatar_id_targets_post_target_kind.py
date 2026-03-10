from typing import Literal, cast

BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind = Literal[
    "analyzed_avatar_3d", "avatar_3d", "coarse_pointcloud_3d", "imageset_2d", "mesh_3d", "report"
]

BODY_START_TARGET_CREATION_API_V2_VIATARS_VIATAR_ID_TARGETS_POST_TARGET_KIND_VALUES: set[
    BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind
] = {
    "analyzed_avatar_3d",
    "avatar_3d",
    "coarse_pointcloud_3d",
    "imageset_2d",
    "mesh_3d",
    "report",
}


def check_body_start_target_creation_api_v2_viatars_viatar_id_targets_post_target_kind(
    value: str,
) -> BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind:
    if value in BODY_START_TARGET_CREATION_API_V2_VIATARS_VIATAR_ID_TARGETS_POST_TARGET_KIND_VALUES:
        return cast(BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_START_TARGET_CREATION_API_V2_VIATARS_VIATAR_ID_TARGETS_POST_TARGET_KIND_VALUES!r}"
    )
