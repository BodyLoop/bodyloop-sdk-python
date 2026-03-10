from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_data import UserData


T = TypeVar("T", bound="BodyCreateUserApiV2AuthentificationUsersPost")


@_attrs_define
class BodyCreateUserApiV2AuthentificationUsersPost:
    user_data: UserData | Unset = UNSET
    """ UserData """
    password: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_data, Unset):
            user_data = self.user_data.to_dict()

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_data import UserData

        d = dict(src_dict)
        _user_data = d.pop("user_data", UNSET)
        user_data: UserData | Unset
        if isinstance(_user_data, Unset):
            user_data = UNSET
        else:
            user_data = UserData.from_dict(_user_data)

        password = d.pop("password", UNSET)

        body_create_user_api_v2_authentification_users_post = cls(
            user_data=user_data,
            password=password,
        )

        body_create_user_api_v2_authentification_users_post.additional_properties = d
        return body_create_user_api_v2_authentification_users_post

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
