from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyFactoryResetApiV2SystemFactoryResetPost")


@_attrs_define
class BodyFactoryResetApiV2SystemFactoryResetPost:
    dongle_serial: str | Unset = UNSET
    data: bool | Unset = False
    system: bool | Unset = False
    user: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dongle_serial = self.dongle_serial

        data = self.data

        system = self.system

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dongle_serial is not UNSET:
            field_dict["dongle_serial"] = dongle_serial
        if data is not UNSET:
            field_dict["data"] = data
        if system is not UNSET:
            field_dict["system"] = system
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dongle_serial = d.pop("dongle_serial", UNSET)

        data = d.pop("data", UNSET)

        system = d.pop("system", UNSET)

        user = d.pop("user", UNSET)

        body_factory_reset_api_v2_system_factory_reset_post = cls(
            dongle_serial=dongle_serial,
            data=data,
            system=system,
            user=user,
        )

        body_factory_reset_api_v2_system_factory_reset_post.additional_properties = d
        return body_factory_reset_api_v2_system_factory_reset_post

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
