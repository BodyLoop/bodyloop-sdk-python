from typing import Literal, cast

UserDataUserGroup = Literal["admin", "operator"]

USER_DATA_USER_GROUP_VALUES: set[UserDataUserGroup] = {
    "admin",
    "operator",
}


def check_user_data_user_group(value: str) -> UserDataUserGroup:
    if value in USER_DATA_USER_GROUP_VALUES:
        return cast(UserDataUserGroup, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_DATA_USER_GROUP_VALUES!r}")
