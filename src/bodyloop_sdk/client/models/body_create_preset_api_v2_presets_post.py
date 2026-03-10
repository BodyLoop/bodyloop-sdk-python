from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyCreatePresetApiV2PresetsPost")


@_attrs_define
class BodyCreatePresetApiV2PresetsPost:
    viatar_id: int | Unset = UNSET
    label: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        viatar_id = self.viatar_id

        label = self.label

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if viatar_id is not UNSET:
            field_dict["viatar_id"] = viatar_id
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        viatar_id = d.pop("viatar_id", UNSET)

        label = d.pop("label", UNSET)

        note = d.pop("note", UNSET)

        body_create_preset_api_v2_presets_post = cls(
            viatar_id=viatar_id,
            label=label,
            note=note,
        )

        body_create_preset_api_v2_presets_post.additional_properties = d
        return body_create_preset_api_v2_presets_post

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
