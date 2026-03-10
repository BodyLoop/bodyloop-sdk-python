from typing import Literal, cast

SystemDataUpdateStreamType0 = Literal["beta", "snapshot", "stable"]

SYSTEM_DATA_UPDATE_STREAM_TYPE_0_VALUES: set[SystemDataUpdateStreamType0] = {
    "beta",
    "snapshot",
    "stable",
}


def check_system_data_update_stream_type_0(value: str) -> SystemDataUpdateStreamType0:
    if value in SYSTEM_DATA_UPDATE_STREAM_TYPE_0_VALUES:
        return cast(SystemDataUpdateStreamType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYSTEM_DATA_UPDATE_STREAM_TYPE_0_VALUES!r}")
