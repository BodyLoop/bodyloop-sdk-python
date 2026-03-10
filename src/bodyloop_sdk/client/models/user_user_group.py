from typing import Literal, cast

UserUserGroup = Literal["admin", "operator"]

USER_USER_GROUP_VALUES: set[UserUserGroup] = {
    "admin",
    "operator",
}


def check_user_user_group(value: str) -> UserUserGroup:
    if value in USER_USER_GROUP_VALUES:
        return cast(UserUserGroup, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_USER_GROUP_VALUES!r}")
