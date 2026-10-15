from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_data_user_group import UserDataUserGroup, check_user_data_user_group
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_data_preferences_type_0 import UserDataPreferencesType0


T = TypeVar("T", bound="UserData")


@_attrs_define
class UserData:
    """UserData"""

    username: str
    full_name: str | Unset = UNSET
    user_group: UserDataUserGroup | Unset = UNSET
    disabled: bool | Unset = False
    preferences: None | Unset | UserDataPreferencesType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_data_preferences_type_0 import UserDataPreferencesType0  # noqa: PLC0415

        username = self.username

        full_name = self.full_name

        user_group: str | Unset = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group

        disabled = self.disabled

        preferences: dict[str, Any] | None | Unset
        if isinstance(self.preferences, Unset):
            preferences = UNSET
        elif isinstance(self.preferences, UserDataPreferencesType0):
            preferences = self.preferences.to_dict()
        else:
            preferences = self.preferences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if user_group is not UNSET:
            field_dict["user_group"] = user_group
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_data_preferences_type_0 import UserDataPreferencesType0  # noqa: PLC0415

        d = dict(src_dict)
        username = d.pop("username")

        full_name = d.pop("full_name", UNSET)

        _user_group = d.pop("user_group", UNSET)
        user_group: UserDataUserGroup | Unset
        if isinstance(_user_group, Unset):
            user_group = UNSET
        else:
            user_group = check_user_data_user_group(_user_group)

        disabled = d.pop("disabled", UNSET)

        def _parse_preferences(data: object) -> None | Unset | UserDataPreferencesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preferences_type_0 = UserDataPreferencesType0.from_dict(data)

                return preferences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserDataPreferencesType0, data)

        preferences = _parse_preferences(d.pop("preferences", UNSET))

        user_data = cls(
            username=username,
            full_name=full_name,
            user_group=user_group,
            disabled=disabled,
            preferences=preferences,
        )

        user_data.additional_properties = d
        return user_data

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
