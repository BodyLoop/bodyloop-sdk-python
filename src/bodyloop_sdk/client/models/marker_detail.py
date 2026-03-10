from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marker_detail_marker_type_type_0 import (
    MarkerDetailMarkerTypeType0,
    check_marker_detail_marker_type_type_0,
)
from ..models.marker_detail_overriding_type_0 import MarkerDetailOverridingType0, check_marker_detail_overriding_type_0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marker_detail_refering_measures import MarkerDetailReferingMeasures


T = TypeVar("T", bound="MarkerDetail")


@_attrs_define
class MarkerDetail:
    """Extended version of `Marker` that includes refering_measures and overriding infomation

    Example:
        {'hidden': False, 'key_external': '', 'label': 'Descriptive label', 'marker_path': 'custom.path.M', 'normal':
            [0, 0.0, 1.0], 'note': 'Meaningful description...', 'position': [0.0, 0.0, 1.0]}

    """

    marker_type: MarkerDetailMarkerTypeType0 | None | Unset = UNSET
    marker_path: str | Unset = UNSET
    position: list[float] | None | Unset = UNSET
    normal: list[float] | None | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    refering_measures: MarkerDetailReferingMeasures | Unset = UNSET
    overriding: MarkerDetailOverridingType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        marker_type: None | str | Unset
        if isinstance(self.marker_type, Unset):
            marker_type = UNSET
        elif isinstance(self.marker_type, str):
            marker_type = self.marker_type
        else:
            marker_type = self.marker_type

        marker_path = self.marker_path

        position: list[float] | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, list):
            position = []
            for position_type_0_item_data in self.position:
                position_type_0_item: float
                position_type_0_item = position_type_0_item_data
                position.append(position_type_0_item)

        else:
            position = self.position

        normal: list[float] | None | Unset
        if isinstance(self.normal, Unset):
            normal = UNSET
        elif isinstance(self.normal, list):
            normal = []
            for normal_type_0_item_data in self.normal:
                normal_type_0_item: float
                normal_type_0_item = normal_type_0_item_data
                normal.append(normal_type_0_item)

        else:
            normal = self.normal

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

        style: None | str | Unset
        if isinstance(self.style, Unset):
            style = UNSET
        else:
            style = self.style

        key_external: None | str | Unset
        if isinstance(self.key_external, Unset):
            key_external = UNSET
        else:
            key_external = self.key_external

        hidden: bool | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        else:
            hidden = self.hidden

        refering_measures: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refering_measures, Unset):
            refering_measures = self.refering_measures.to_dict()

        overriding: None | str | Unset
        if isinstance(self.overriding, Unset):
            overriding = UNSET
        elif isinstance(self.overriding, str):
            overriding = self.overriding
        else:
            overriding = self.overriding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if marker_type is not UNSET:
            field_dict["marker_type"] = marker_type
        if marker_path is not UNSET:
            field_dict["marker_path"] = marker_path
        if position is not UNSET:
            field_dict["position"] = position
        if normal is not UNSET:
            field_dict["normal"] = normal
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note
        if style is not UNSET:
            field_dict["style"] = style
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if refering_measures is not UNSET:
            field_dict["refering_measures"] = refering_measures
        if overriding is not UNSET:
            field_dict["overriding"] = overriding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marker_detail_refering_measures import MarkerDetailReferingMeasures

        d = dict(src_dict)

        def _parse_marker_type(data: object) -> MarkerDetailMarkerTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marker_type_type_0 = check_marker_detail_marker_type_type_0(data)

                return marker_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarkerDetailMarkerTypeType0 | None | Unset, data)

        marker_type = _parse_marker_type(d.pop("marker_type", UNSET))

        marker_path = d.pop("marker_path", UNSET)

        def _parse_position(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                position_type_0 = []
                _position_type_0 = data
                for position_type_0_item_data in _position_type_0:

                    def _parse_position_type_0_item(data: object) -> float:
                        return cast(float, data)

                    position_type_0_item = _parse_position_type_0_item(position_type_0_item_data)

                    position_type_0.append(position_type_0_item)

                return position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_normal(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                normal_type_0 = []
                _normal_type_0 = data
                for normal_type_0_item_data in _normal_type_0:

                    def _parse_normal_type_0_item(data: object) -> float:
                        return cast(float, data)

                    normal_type_0_item = _parse_normal_type_0_item(normal_type_0_item_data)

                    normal_type_0.append(normal_type_0_item)

                return normal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        normal = _parse_normal(d.pop("normal", UNSET))

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

        def _parse_style(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        style = _parse_style(d.pop("style", UNSET))

        def _parse_key_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_external = _parse_key_external(d.pop("key_external", UNSET))

        def _parse_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))

        _refering_measures = d.pop("refering_measures", UNSET)
        refering_measures: MarkerDetailReferingMeasures | Unset
        if isinstance(_refering_measures, Unset):
            refering_measures = UNSET
        else:
            refering_measures = MarkerDetailReferingMeasures.from_dict(_refering_measures)

        def _parse_overriding(data: object) -> MarkerDetailOverridingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                overriding_type_0 = check_marker_detail_overriding_type_0(data)

                return overriding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarkerDetailOverridingType0 | None | Unset, data)

        overriding = _parse_overriding(d.pop("overriding", UNSET))

        marker_detail = cls(
            marker_type=marker_type,
            marker_path=marker_path,
            position=position,
            normal=normal,
            label=label,
            note=note,
            style=style,
            key_external=key_external,
            hidden=hidden,
            refering_measures=refering_measures,
            overriding=overriding,
        )

        marker_detail.additional_properties = d
        return marker_detail

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
