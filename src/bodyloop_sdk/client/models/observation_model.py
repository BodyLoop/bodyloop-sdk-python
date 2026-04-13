from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObservationModel")


@_attrs_define
class ObservationModel:
    source: Literal["PHD"] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: Literal["PHD"] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_source(data: object) -> Literal["PHD"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            source_type_0 = cast(Literal["PHD"], data)
            if source_type_0 != "PHD":
                raise ValueError(f"source_type_0 must match const 'PHD', got '{source_type_0}'")
            return source_type_0
            return cast(Literal["PHD"] | None | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        observation_model = cls(
            source=source,
        )

        observation_model.additional_properties = d
        return observation_model

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
