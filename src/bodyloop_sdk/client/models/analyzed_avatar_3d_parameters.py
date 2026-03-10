from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyzedAvatar3DParameters")


@_attrs_define
class AnalyzedAvatar3DParameters:
    """Parameters influencing the target AnalyzedAvatar3D"""

    preset_id: int | None | Unset = UNSET
    palp_snap_distance: float | None | Unset = UNSET
    orphaned_palpation_marker: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preset_id: int | None | Unset
        if isinstance(self.preset_id, Unset):
            preset_id = UNSET
        else:
            preset_id = self.preset_id

        palp_snap_distance: float | None | Unset
        if isinstance(self.palp_snap_distance, Unset):
            palp_snap_distance = UNSET
        else:
            palp_snap_distance = self.palp_snap_distance

        orphaned_palpation_marker: bool | None | Unset
        if isinstance(self.orphaned_palpation_marker, Unset):
            orphaned_palpation_marker = UNSET
        else:
            orphaned_palpation_marker = self.orphaned_palpation_marker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preset_id is not UNSET:
            field_dict["preset_id"] = preset_id
        if palp_snap_distance is not UNSET:
            field_dict["palp_snap_distance"] = palp_snap_distance
        if orphaned_palpation_marker is not UNSET:
            field_dict["orphaned_palpation_marker"] = orphaned_palpation_marker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_preset_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        preset_id = _parse_preset_id(d.pop("preset_id", UNSET))

        def _parse_palp_snap_distance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        palp_snap_distance = _parse_palp_snap_distance(d.pop("palp_snap_distance", UNSET))

        def _parse_orphaned_palpation_marker(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        orphaned_palpation_marker = _parse_orphaned_palpation_marker(d.pop("orphaned_palpation_marker", UNSET))

        analyzed_avatar_3d_parameters = cls(
            preset_id=preset_id,
            palp_snap_distance=palp_snap_distance,
            orphaned_palpation_marker=orphaned_palpation_marker,
        )

        analyzed_avatar_3d_parameters.additional_properties = d
        return analyzed_avatar_3d_parameters

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
