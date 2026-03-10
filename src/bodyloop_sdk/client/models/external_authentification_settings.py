from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalAuthentificationSettings")


@_attrs_define
class ExternalAuthentificationSettings:
    """Settings for external authentification"""

    oauth_client_id: None | str | Unset = UNSET
    oauth_device_auth_endpoint: None | str | Unset = UNSET
    oauth_device_token_endpoint: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth_client_id: None | str | Unset
        if isinstance(self.oauth_client_id, Unset):
            oauth_client_id = UNSET
        else:
            oauth_client_id = self.oauth_client_id

        oauth_device_auth_endpoint: None | str | Unset
        if isinstance(self.oauth_device_auth_endpoint, Unset):
            oauth_device_auth_endpoint = UNSET
        else:
            oauth_device_auth_endpoint = self.oauth_device_auth_endpoint

        oauth_device_token_endpoint: None | str | Unset
        if isinstance(self.oauth_device_token_endpoint, Unset):
            oauth_device_token_endpoint = UNSET
        else:
            oauth_device_token_endpoint = self.oauth_device_token_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oauth_client_id is not UNSET:
            field_dict["oauth_client_id"] = oauth_client_id
        if oauth_device_auth_endpoint is not UNSET:
            field_dict["oauth_device_auth_endpoint"] = oauth_device_auth_endpoint
        if oauth_device_token_endpoint is not UNSET:
            field_dict["oauth_device_token_endpoint"] = oauth_device_token_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_oauth_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oauth_client_id = _parse_oauth_client_id(d.pop("oauth_client_id", UNSET))

        def _parse_oauth_device_auth_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oauth_device_auth_endpoint = _parse_oauth_device_auth_endpoint(d.pop("oauth_device_auth_endpoint", UNSET))

        def _parse_oauth_device_token_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oauth_device_token_endpoint = _parse_oauth_device_token_endpoint(d.pop("oauth_device_token_endpoint", UNSET))

        external_authentification_settings = cls(
            oauth_client_id=oauth_client_id,
            oauth_device_auth_endpoint=oauth_device_auth_endpoint,
            oauth_device_token_endpoint=oauth_device_token_endpoint,
        )

        external_authentification_settings.additional_properties = d
        return external_authentification_settings

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
