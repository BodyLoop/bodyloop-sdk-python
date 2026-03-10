from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportParameters")


@_attrs_define
class ReportParameters:
    """Parameters influencing the target Report"""

    preset: Literal["Default"] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preset: Literal["Default"] | None | Unset
        if isinstance(self.preset, Unset):
            preset = UNSET
        else:
            preset = self.preset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preset is not UNSET:
            field_dict["preset"] = preset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_preset(data: object) -> Literal["Default"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            preset_type_0 = cast(Literal["Default"], data)
            if preset_type_0 != "Default":
                raise ValueError(f"preset_type_0 must match const 'Default', got '{preset_type_0}'")
            return preset_type_0
            return cast(Literal["Default"] | None | Unset, data)

        preset = _parse_preset(d.pop("preset", UNSET))

        report_parameters = cls(
            preset=preset,
        )

        report_parameters.additional_properties = d
        return report_parameters

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
