from typing import Literal, cast

SystemUpdateStreamType0 = Literal["beta", "snapshot", "stable"]

SYSTEM_UPDATE_STREAM_TYPE_0_VALUES: set[SystemUpdateStreamType0] = {
    "beta",
    "snapshot",
    "stable",
}


def check_system_update_stream_type_0(value: str) -> SystemUpdateStreamType0:
    if value in SYSTEM_UPDATE_STREAM_TYPE_0_VALUES:
        return cast(SystemUpdateStreamType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYSTEM_UPDATE_STREAM_TYPE_0_VALUES!r}")
