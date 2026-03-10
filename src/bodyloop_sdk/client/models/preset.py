from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.angle import Angle
    from ..models.axis import Axis
    from ..models.crosssection import Crosssection
    from ..models.distance import Distance
    from ..models.height import Height
    from ..models.marker import Marker
    from ..models.meta import Meta
    from ..models.property_ import Property


T = TypeVar("T", bound="Preset")


@_attrs_define
class Preset:
    """Extended version of `PresetData` that includes unique preset_id and meta information."""

    preset_id: int
    properties: list[Property] | Unset = UNSET
    auto_marker: list[Marker] | Unset = UNSET
    palpation_marker: list[Marker] | Unset = UNSET
    custom_marker: list[Marker] | Unset = UNSET
    heights: list[Height] | Unset = UNSET
    distances: list[Distance] | Unset = UNSET
    angles: list[Angle] | Unset = UNSET
    crosssections: list[Crosssection] | Unset = UNSET
    axes: list[Axis] | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta

        preset_id = self.preset_id

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        auto_marker: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auto_marker, Unset):
            auto_marker = []
            for auto_marker_item_data in self.auto_marker:
                auto_marker_item = auto_marker_item_data.to_dict()
                auto_marker.append(auto_marker_item)

        palpation_marker: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.palpation_marker, Unset):
            palpation_marker = []
            for palpation_marker_item_data in self.palpation_marker:
                palpation_marker_item = palpation_marker_item_data.to_dict()
                palpation_marker.append(palpation_marker_item)

        custom_marker: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_marker, Unset):
            custom_marker = []
            for custom_marker_item_data in self.custom_marker:
                custom_marker_item = custom_marker_item_data.to_dict()
                custom_marker.append(custom_marker_item)

        heights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.heights, Unset):
            heights = []
            for heights_item_data in self.heights:
                heights_item = heights_item_data.to_dict()
                heights.append(heights_item)

        distances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.distances, Unset):
            distances = []
            for distances_item_data in self.distances:
                distances_item = distances_item_data.to_dict()
                distances.append(distances_item)

        angles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.angles, Unset):
            angles = []
            for angles_item_data in self.angles:
                angles_item = angles_item_data.to_dict()
                angles.append(angles_item)

        crosssections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.crosssections, Unset):
            crosssections = []
            for crosssections_item_data in self.crosssections:
                crosssections_item = crosssections_item_data.to_dict()
                crosssections.append(crosssections_item)

        axes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.axes, Unset):
            axes = []
            for axes_item_data in self.axes:
                axes_item = axes_item_data.to_dict()
                axes.append(axes_item)

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

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, Meta):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preset_id": preset_id,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties
        if auto_marker is not UNSET:
            field_dict["autoMarker"] = auto_marker
        if palpation_marker is not UNSET:
            field_dict["palpationMarker"] = palpation_marker
        if custom_marker is not UNSET:
            field_dict["customMarker"] = custom_marker
        if heights is not UNSET:
            field_dict["heights"] = heights
        if distances is not UNSET:
            field_dict["distances"] = distances
        if angles is not UNSET:
            field_dict["angles"] = angles
        if crosssections is not UNSET:
            field_dict["crosssections"] = crosssections
        if axes is not UNSET:
            field_dict["axes"] = axes
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.angle import Angle
        from ..models.axis import Axis
        from ..models.crosssection import Crosssection
        from ..models.distance import Distance
        from ..models.height import Height
        from ..models.marker import Marker
        from ..models.meta import Meta
        from ..models.property_ import Property

        d = dict(src_dict)
        preset_id = d.pop("preset_id")

        _properties = d.pop("properties", UNSET)
        properties: list[Property] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = Property.from_dict(properties_item_data)

                properties.append(properties_item)

        _auto_marker = d.pop("autoMarker", UNSET)
        auto_marker: list[Marker] | Unset = UNSET
        if _auto_marker is not UNSET:
            auto_marker = []
            for auto_marker_item_data in _auto_marker:
                auto_marker_item = Marker.from_dict(auto_marker_item_data)

                auto_marker.append(auto_marker_item)

        _palpation_marker = d.pop("palpationMarker", UNSET)
        palpation_marker: list[Marker] | Unset = UNSET
        if _palpation_marker is not UNSET:
            palpation_marker = []
            for palpation_marker_item_data in _palpation_marker:
                palpation_marker_item = Marker.from_dict(palpation_marker_item_data)

                palpation_marker.append(palpation_marker_item)

        _custom_marker = d.pop("customMarker", UNSET)
        custom_marker: list[Marker] | Unset = UNSET
        if _custom_marker is not UNSET:
            custom_marker = []
            for custom_marker_item_data in _custom_marker:
                custom_marker_item = Marker.from_dict(custom_marker_item_data)

                custom_marker.append(custom_marker_item)

        _heights = d.pop("heights", UNSET)
        heights: list[Height] | Unset = UNSET
        if _heights is not UNSET:
            heights = []
            for heights_item_data in _heights:
                heights_item = Height.from_dict(heights_item_data)

                heights.append(heights_item)

        _distances = d.pop("distances", UNSET)
        distances: list[Distance] | Unset = UNSET
        if _distances is not UNSET:
            distances = []
            for distances_item_data in _distances:
                distances_item = Distance.from_dict(distances_item_data)

                distances.append(distances_item)

        _angles = d.pop("angles", UNSET)
        angles: list[Angle] | Unset = UNSET
        if _angles is not UNSET:
            angles = []
            for angles_item_data in _angles:
                angles_item = Angle.from_dict(angles_item_data)

                angles.append(angles_item)

        _crosssections = d.pop("crosssections", UNSET)
        crosssections: list[Crosssection] | Unset = UNSET
        if _crosssections is not UNSET:
            crosssections = []
            for crosssections_item_data in _crosssections:
                crosssections_item = Crosssection.from_dict(crosssections_item_data)

                crosssections.append(crosssections_item)

        _axes = d.pop("axes", UNSET)
        axes: list[Axis] | Unset = UNSET
        if _axes is not UNSET:
            axes = []
            for axes_item_data in _axes:
                axes_item = Axis.from_dict(axes_item_data)

                axes.append(axes_item)

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

        def _parse_meta(data: object) -> Meta | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = Meta.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Meta | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        preset = cls(
            preset_id=preset_id,
            properties=properties,
            auto_marker=auto_marker,
            palpation_marker=palpation_marker,
            custom_marker=custom_marker,
            heights=heights,
            distances=distances,
            angles=angles,
            crosssections=crosssections,
            axes=axes,
            label=label,
            note=note,
            key_external=key_external,
            meta=meta,
        )

        preset.additional_properties = d
        return preset

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
