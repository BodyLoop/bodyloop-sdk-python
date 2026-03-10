from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyCreateFirstAdminApiV2AuthentificationUsersFirstAdminPost")


@_attrs_define
class BodyCreateFirstAdminApiV2AuthentificationUsersFirstAdminPost:
    username: str | Unset = UNSET
    full_name: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        full_name = self.full_name

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        full_name = d.pop("full_name", UNSET)

        password = d.pop("password", UNSET)

        body_create_first_admin_api_v2_authentification_users_first_admin_post = cls(
            username=username,
            full_name=full_name,
            password=password,
        )

        body_create_first_admin_api_v2_authentification_users_first_admin_post.additional_properties = d
        return body_create_first_admin_api_v2_authentification_users_first_admin_post

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
