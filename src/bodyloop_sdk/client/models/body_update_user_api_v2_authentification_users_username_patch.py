from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.body_update_user_api_v2_authentification_users_username_patch_user_group_type_0 import (
    BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0,
    check_body_update_user_api_v2_authentification_users_username_patch_user_group_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyUpdateUserApiV2AuthentificationUsersUsernamePatch")


@_attrs_define
class BodyUpdateUserApiV2AuthentificationUsersUsernamePatch:
    full_name: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    user_group: BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0 | None | Unset = UNSET
    disabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        user_group: None | str | Unset
        if isinstance(self.user_group, Unset):
            user_group = UNSET
        elif isinstance(self.user_group, str):
            user_group = self.user_group
        else:
            user_group = self.user_group

        disabled: bool | None | Unset
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if password is not UNSET:
            field_dict["password"] = password
        if user_group is not UNSET:
            field_dict["user_group"] = user_group
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_user_group(
            data: object,
        ) -> BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_group_type_0 = (
                    check_body_update_user_api_v2_authentification_users_username_patch_user_group_type_0(data)
                )

                return user_group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0 | None | Unset, data)

        user_group = _parse_user_group(d.pop("user_group", UNSET))

        def _parse_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))

        body_update_user_api_v2_authentification_users_username_patch = cls(
            full_name=full_name,
            password=password,
            user_group=user_group,
            disabled=disabled,
        )

        body_update_user_api_v2_authentification_users_username_patch.additional_properties = d
        return body_update_user_api_v2_authentification_users_username_patch

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
