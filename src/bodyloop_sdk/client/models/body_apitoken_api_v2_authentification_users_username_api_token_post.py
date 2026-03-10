from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost")


@_attrs_define
class BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost:
    expires_in: int | Unset = UNSET
    apitoken_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in = self.expires_in

        apitoken_name = self.apitoken_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if apitoken_name is not UNSET:
            field_dict["apitoken_name"] = apitoken_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_in = d.pop("expires_in", UNSET)

        apitoken_name = d.pop("apitoken_name", UNSET)

        body_apitoken_api_v2_authentification_users_username_api_token_post = cls(
            expires_in=expires_in,
            apitoken_name=apitoken_name,
        )

        body_apitoken_api_v2_authentification_users_username_api_token_post.additional_properties = d
        return body_apitoken_api_v2_authentification_users_username_api_token_post

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
