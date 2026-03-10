from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distance_distances_type_0 import DistanceDistancesType0


T = TypeVar("T", bound="Distance")


@_attrs_define
class Distance:
    """Distance representation between two markers

    Example:
        {'distance_path': 'custom.path.M', 'from_marker': 'marker_a', 'hidden': False, 'key_external': '', 'label':
            'Descriptive label', 'note': 'Meaningful description...', 'to_marker': 'marker_b'}

    """

    distance_path: str | Unset = UNSET
    from_marker: str | Unset = UNSET
    to_marker: str | Unset = UNSET
    distances: DistanceDistancesType0 | None | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    preference: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.distance_distances_type_0 import DistanceDistancesType0

        distance_path = self.distance_path

        from_marker = self.from_marker

        to_marker = self.to_marker

        distances: dict[str, Any] | None | Unset
        if isinstance(self.distances, Unset):
            distances = UNSET
        elif isinstance(self.distances, DistanceDistancesType0):
            distances = self.distances.to_dict()
        else:
            distances = self.distances

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

        preference: None | str | Unset
        if isinstance(self.preference, Unset):
            preference = UNSET
        else:
            preference = self.preference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance_path is not UNSET:
            field_dict["distance_path"] = distance_path
        if from_marker is not UNSET:
            field_dict["from_marker"] = from_marker
        if to_marker is not UNSET:
            field_dict["to_marker"] = to_marker
        if distances is not UNSET:
            field_dict["distances"] = distances
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
        if preference is not UNSET:
            field_dict["preference"] = preference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.distance_distances_type_0 import DistanceDistancesType0

        d = dict(src_dict)
        distance_path = d.pop("distance_path", UNSET)

        from_marker = d.pop("from_marker", UNSET)

        to_marker = d.pop("to_marker", UNSET)

        def _parse_distances(data: object) -> DistanceDistancesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distances_type_0 = DistanceDistancesType0.from_dict(data)

                return distances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DistanceDistancesType0 | None | Unset, data)

        distances = _parse_distances(d.pop("distances", UNSET))

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

        def _parse_preference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preference = _parse_preference(d.pop("preference", UNSET))

        distance = cls(
            distance_path=distance_path,
            from_marker=from_marker,
            to_marker=to_marker,
            distances=distances,
            label=label,
            note=note,
            style=style,
            key_external=key_external,
            hidden=hidden,
            preference=preference,
        )

        distance.additional_properties = d
        return distance

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
