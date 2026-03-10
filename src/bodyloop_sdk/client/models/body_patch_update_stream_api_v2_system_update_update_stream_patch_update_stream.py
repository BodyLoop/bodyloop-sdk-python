from typing import Literal, cast

BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream = Literal["beta", "stable"]

BODY_PATCH_UPDATE_STREAM_API_V2_SYSTEM_UPDATE_UPDATE_STREAM_PATCH_UPDATE_STREAM_VALUES: set[
    BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream
] = {
    "beta",
    "stable",
}


def check_body_patch_update_stream_api_v2_system_update_update_stream_patch_update_stream(
    value: str,
) -> BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream:
    if value in BODY_PATCH_UPDATE_STREAM_API_V2_SYSTEM_UPDATE_UPDATE_STREAM_PATCH_UPDATE_STREAM_VALUES:
        return cast(BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_PATCH_UPDATE_STREAM_API_V2_SYSTEM_UPDATE_UPDATE_STREAM_PATCH_UPDATE_STREAM_VALUES!r}"
    )
