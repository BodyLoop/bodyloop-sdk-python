from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.angle_angles_type_0 import AngleAnglesType0


T = TypeVar("T", bound="Angle")


@_attrs_define
class Angle:
    """Angle representation between three markers

    Example:
        {'angle_path': 'custom.path.M', 'at_marker': 'marker_o', 'from_marker': 'marker_a', 'hidden': False,
            'key_external': '', 'label': 'Descriptive label', 'note': 'Meaningful description...', 'to_marker': 'marker_b'}

    """

    angle_path: str | Unset = UNSET
    label: None | str | Unset = UNSET
    at_marker: str | Unset = UNSET
    from_marker: str | Unset = UNSET
    to_marker: str | Unset = UNSET
    angles: AngleAnglesType0 | None | Unset = UNSET
    note: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    preference: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.angle_angles_type_0 import AngleAnglesType0

        angle_path = self.angle_path

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        at_marker = self.at_marker

        from_marker = self.from_marker

        to_marker = self.to_marker

        angles: dict[str, Any] | None | Unset
        if isinstance(self.angles, Unset):
            angles = UNSET
        elif isinstance(self.angles, AngleAnglesType0):
            angles = self.angles.to_dict()
        else:
            angles = self.angles

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

        preference: None | str | Unset
        if isinstance(self.preference, Unset):
            preference = UNSET
        else:
            preference = self.preference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angle_path is not UNSET:
            field_dict["angle_path"] = angle_path
        if label is not UNSET:
            field_dict["label"] = label
        if at_marker is not UNSET:
            field_dict["at_marker"] = at_marker
        if from_marker is not UNSET:
            field_dict["from_marker"] = from_marker
        if to_marker is not UNSET:
            field_dict["to_marker"] = to_marker
        if angles is not UNSET:
            field_dict["angles"] = angles
        if note is not UNSET:
            field_dict["note"] = note
        if style is not UNSET:
            field_dict["style"] = style
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if preference is not UNSET:
            field_dict["preference"] = preference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.angle_angles_type_0 import AngleAnglesType0

        d = dict(src_dict)
        angle_path = d.pop("angle_path", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        at_marker = d.pop("at_marker", UNSET)

        from_marker = d.pop("from_marker", UNSET)

        to_marker = d.pop("to_marker", UNSET)

        def _parse_angles(data: object) -> AngleAnglesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                angles_type_0 = AngleAnglesType0.from_dict(data)

                return angles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AngleAnglesType0 | None | Unset, data)

        angles = _parse_angles(d.pop("angles", UNSET))

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

        def _parse_preference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preference = _parse_preference(d.pop("preference", UNSET))

        angle = cls(
            angle_path=angle_path,
            label=label,
            at_marker=at_marker,
            from_marker=from_marker,
            to_marker=to_marker,
            angles=angles,
            note=note,
            style=style,
            key_external=key_external,
            hidden=hidden,
            preference=preference,
        )

        angle.additional_properties = d
        return angle

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
