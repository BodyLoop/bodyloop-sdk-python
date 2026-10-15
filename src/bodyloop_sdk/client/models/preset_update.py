from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preset_update_attributes_external_type_0 import PresetUpdateAttributesExternalType0


T = TypeVar("T", bound="PresetUpdate")


@_attrs_define
class PresetUpdate:
    """Descriptive fields of a preset that can be changed via PATCH.
    Only explicitly set fields are applied, `None` clears a field.

    """

    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    attributes_external: None | PresetUpdateAttributesExternalType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.preset_update_attributes_external_type_0 import PresetUpdateAttributesExternalType0  # noqa: PLC0415

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        key_external: None | str | Unset
        if isinstance(self.key_external, Unset):
            key_external = UNSET
        else:
            key_external = self.key_external

        attributes_external: dict[str, Any] | None | Unset
        if isinstance(self.attributes_external, Unset):
            attributes_external = UNSET
        elif isinstance(self.attributes_external, PresetUpdateAttributesExternalType0):
            attributes_external = self.attributes_external.to_dict()
        else:
            attributes_external = self.attributes_external

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if attributes_external is not UNSET:
            field_dict["attributes_external"] = attributes_external

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preset_update_attributes_external_type_0 import PresetUpdateAttributesExternalType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_key_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_external = _parse_key_external(d.pop("key_external", UNSET))

        def _parse_attributes_external(data: object) -> None | PresetUpdateAttributesExternalType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_external_type_0 = PresetUpdateAttributesExternalType0.from_dict(data)

                return attributes_external_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PresetUpdateAttributesExternalType0 | Unset, data)

        attributes_external = _parse_attributes_external(d.pop("attributes_external", UNSET))

        preset_update = cls(
            label=label,
            note=note,
            key_external=key_external,
            attributes_external=attributes_external,
        )

        preset_update.additional_properties = d
        return preset_update

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
