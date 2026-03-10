from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemOsData")


@_attrs_define
class SystemOsData:
    """System OS information and configuration"""

    keyboard_layout: None | str | Unset = UNSET
    hostname: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyboard_layout: None | str | Unset
        if isinstance(self.keyboard_layout, Unset):
            keyboard_layout = UNSET
        else:
            keyboard_layout = self.keyboard_layout

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyboard_layout is not UNSET:
            field_dict["keyboard_layout"] = keyboard_layout
        if hostname is not UNSET:
            field_dict["hostname"] = hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_keyboard_layout(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keyboard_layout = _parse_keyboard_layout(d.pop("keyboard_layout", UNSET))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        system_os_data = cls(
            keyboard_layout=keyboard_layout,
            hostname=hostname,
        )

        system_os_data.additional_properties = d
        return system_os_data

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
