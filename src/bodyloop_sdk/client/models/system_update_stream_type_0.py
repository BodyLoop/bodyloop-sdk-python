from typing import Literal

SystemUpdateStreamType0 = Literal["beta", "snapshot", "stable"]

SYSTEM_UPDATE_STREAM_TYPE_0_VALUES: set[SystemUpdateStreamType0] = {
    "beta",
    "snapshot",
    "stable",
}


def check_system_update_stream_type_0(value: str) -> SystemUpdateStreamType0:
    if value in SYSTEM_UPDATE_STREAM_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYSTEM_UPDATE_STREAM_TYPE_0_VALUES!r}")
