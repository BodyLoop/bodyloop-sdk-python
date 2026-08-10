from typing import Literal

TargetStateStatusType0 = Literal["Aborted", "Deleted", "Failed", "Generating", "Pending", "Preparing", "Ready"]

TARGET_STATE_STATUS_TYPE_0_VALUES: set[TargetStateStatusType0] = {
    "Aborted",
    "Deleted",
    "Failed",
    "Generating",
    "Pending",
    "Preparing",
    "Ready",
}


def check_target_state_status_type_0(value: str) -> TargetStateStatusType0:
    if value in TARGET_STATE_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TARGET_STATE_STATUS_TYPE_0_VALUES!r}")
