from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_os_network_interfaces_type_0 import SystemOsNetworkInterfacesType0


T = TypeVar("T", bound="SystemOs")


@_attrs_define
class SystemOs:
    """Extended version of `SystemOsData` that includes all os read-only settings."""

    keyboard_layout: None | str | Unset = UNSET
    hostname: None | str | Unset = UNSET
    network_interfaces: None | SystemOsNetworkInterfacesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_os_network_interfaces_type_0 import SystemOsNetworkInterfacesType0

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

        network_interfaces: dict[str, Any] | None | Unset
        if isinstance(self.network_interfaces, Unset):
            network_interfaces = UNSET
        elif isinstance(self.network_interfaces, SystemOsNetworkInterfacesType0):
            network_interfaces = self.network_interfaces.to_dict()
        else:
            network_interfaces = self.network_interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyboard_layout is not UNSET:
            field_dict["keyboard_layout"] = keyboard_layout
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if network_interfaces is not UNSET:
            field_dict["network_interfaces"] = network_interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_os_network_interfaces_type_0 import SystemOsNetworkInterfacesType0

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

        def _parse_network_interfaces(data: object) -> None | SystemOsNetworkInterfacesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                network_interfaces_type_0 = SystemOsNetworkInterfacesType0.from_dict(data)

                return network_interfaces_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemOsNetworkInterfacesType0 | Unset, data)

        network_interfaces = _parse_network_interfaces(d.pop("network_interfaces", UNSET))

        system_os = cls(
            keyboard_layout=keyboard_layout,
            hostname=hostname,
            network_interfaces=network_interfaces,
        )

        system_os.additional_properties = d
        return system_os

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
