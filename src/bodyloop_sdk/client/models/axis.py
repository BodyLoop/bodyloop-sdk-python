from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.axis_rotation_type_0 import AxisRotationType0


T = TypeVar("T", bound="Axis")


@_attrs_define
class Axis:
    """Axis representation through two markers

    Example:
        {'axis_path': 'custom.path.M', 'hidden': False, 'key_external': '', 'label': 'Descriptive label', 'markers':
            ['marker_a', 'marker_b'], 'note': 'Meaningful description...'}

    """

    axis_path: str | Unset = UNSET
    markers: list[None | str] | Unset = UNSET
    rotation: AxisRotationType0 | None | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.axis_rotation_type_0 import AxisRotationType0

        axis_path = self.axis_path

        markers: list[None | str] | Unset = UNSET
        if not isinstance(self.markers, Unset):
            markers = []
            for markers_item_data in self.markers:
                markers_item: None | str
                markers_item = markers_item_data
                markers.append(markers_item)

        rotation: dict[str, Any] | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        elif isinstance(self.rotation, AxisRotationType0):
            rotation = self.rotation.to_dict()
        else:
            rotation = self.rotation

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if axis_path is not UNSET:
            field_dict["axis_path"] = axis_path
        if markers is not UNSET:
            field_dict["markers"] = markers
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.axis_rotation_type_0 import AxisRotationType0

        d = dict(src_dict)
        axis_path = d.pop("axis_path", UNSET)

        _markers = d.pop("markers", UNSET)
        markers: list[None | str] | Unset = UNSET
        if _markers is not UNSET:
            markers = []
            for markers_item_data in _markers:

                def _parse_markers_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                markers_item = _parse_markers_item(markers_item_data)

                markers.append(markers_item)

        def _parse_rotation(data: object) -> AxisRotationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rotation_type_0 = AxisRotationType0.from_dict(data)

                return rotation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AxisRotationType0 | None | Unset, data)

        rotation = _parse_rotation(d.pop("rotation", UNSET))

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

        axis = cls(
            axis_path=axis_path,
            markers=markers,
            rotation=rotation,
            label=label,
            note=note,
            style=style,
            key_external=key_external,
            hidden=hidden,
        )

        axis.additional_properties = d
        return axis

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
