from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyApplyPresetApiV2ViatarsViatarIdPresetPut")


@_attrs_define
class BodyApplyPresetApiV2ViatarsViatarIdPresetPut:
    preset_id: int | Unset = UNSET
    additive: bool | Unset = False
    palpation_marker_snap_distance: float | Unset = 0.05
    orphaned_palpation_marker: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preset_id = self.preset_id

        additive = self.additive

        palpation_marker_snap_distance = self.palpation_marker_snap_distance

        orphaned_palpation_marker = self.orphaned_palpation_marker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preset_id is not UNSET:
            field_dict["preset_id"] = preset_id
        if additive is not UNSET:
            field_dict["additive"] = additive
        if palpation_marker_snap_distance is not UNSET:
            field_dict["palpation_marker_snap_distance"] = palpation_marker_snap_distance
        if orphaned_palpation_marker is not UNSET:
            field_dict["orphaned_palpation_marker"] = orphaned_palpation_marker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preset_id = d.pop("preset_id", UNSET)

        additive = d.pop("additive", UNSET)

        palpation_marker_snap_distance = d.pop("palpation_marker_snap_distance", UNSET)

        orphaned_palpation_marker = d.pop("orphaned_palpation_marker", UNSET)

        body_apply_preset_api_v2_viatars_viatar_id_preset_put = cls(
            preset_id=preset_id,
            additive=additive,
            palpation_marker_snap_distance=palpation_marker_snap_distance,
            orphaned_palpation_marker=orphaned_palpation_marker,
        )

        body_apply_preset_api_v2_viatars_viatar_id_preset_put.additional_properties = d
        return body_apply_preset_api_v2_viatars_viatar_id_preset_put

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
