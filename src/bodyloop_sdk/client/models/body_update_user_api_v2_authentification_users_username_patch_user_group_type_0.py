from typing import Literal, cast

BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0 = Literal["admin", "operator"]

BODY_UPDATE_USER_API_V2_AUTHENTIFICATION_USERS_USERNAME_PATCH_USER_GROUP_TYPE_0_VALUES: set[
    BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0
] = {
    "admin",
    "operator",
}


def check_body_update_user_api_v2_authentification_users_username_patch_user_group_type_0(
    value: str,
) -> BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0:
    if value in BODY_UPDATE_USER_API_V2_AUTHENTIFICATION_USERS_USERNAME_PATCH_USER_GROUP_TYPE_0_VALUES:
        return cast(BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_UPDATE_USER_API_V2_AUTHENTIFICATION_USERS_USERNAME_PATCH_USER_GROUP_TYPE_0_VALUES!r}"
    )
