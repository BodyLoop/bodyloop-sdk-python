from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polygonal_chain_preference_type_0 import (
    PolygonalChainPreferenceType0,
    check_polygonal_chain_preference_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polygonal_chain_contours_type_0 import PolygonalChainContoursType0
    from ..models.polygonal_chain_distances_type_0 import PolygonalChainDistancesType0


T = TypeVar("T", bound="PolygonalChain")


@_attrs_define
class PolygonalChain:
    """Polygonal chain representation through an ordered sequence of N (>2) markers

    Example:
        {'hidden': False, 'key_external': '', 'label': 'Descriptive label', 'markers': ['marker_a', 'marker_b',
            'marker_c'], 'note': 'Meaningful description...', 'polygonal_chain_path': 'custom.path.M', 'preference':
            'linear'}

    """

    polygonal_chain_path: str | Unset = UNSET
    markers: list[str] | Unset = UNSET
    distances: None | PolygonalChainDistancesType0 | Unset = UNSET
    contours: None | PolygonalChainContoursType0 | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    preference: None | PolygonalChainPreferenceType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.polygonal_chain_contours_type_0 import PolygonalChainContoursType0  # noqa: PLC0415
        from ..models.polygonal_chain_distances_type_0 import PolygonalChainDistancesType0  # noqa: PLC0415

        polygonal_chain_path = self.polygonal_chain_path

        markers: list[str] | Unset = UNSET
        if not isinstance(self.markers, Unset):
            markers = self.markers

        distances: dict[str, Any] | None | Unset
        if isinstance(self.distances, Unset):
            distances = UNSET
        elif isinstance(self.distances, PolygonalChainDistancesType0):
            distances = self.distances.to_dict()
        else:
            distances = self.distances

        contours: dict[str, Any] | None | Unset
        if isinstance(self.contours, Unset):
            contours = UNSET
        elif isinstance(self.contours, PolygonalChainContoursType0):
            contours = self.contours.to_dict()
        else:
            contours = self.contours

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
        elif isinstance(self.preference, str):
            preference = self.preference
        else:
            preference = self.preference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if polygonal_chain_path is not UNSET:
            field_dict["polygonal_chain_path"] = polygonal_chain_path
        if markers is not UNSET:
            field_dict["markers"] = markers
        if distances is not UNSET:
            field_dict["distances"] = distances
        if contours is not UNSET:
            field_dict["contours"] = contours
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
        from ..models.polygonal_chain_contours_type_0 import PolygonalChainContoursType0  # noqa: PLC0415
        from ..models.polygonal_chain_distances_type_0 import PolygonalChainDistancesType0  # noqa: PLC0415

        d = dict(src_dict)
        polygonal_chain_path = d.pop("polygonal_chain_path", UNSET)

        markers = cast(list[str], d.pop("markers", UNSET))

        def _parse_distances(data: object) -> None | PolygonalChainDistancesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distances_type_0 = PolygonalChainDistancesType0.from_dict(data)

                return distances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolygonalChainDistancesType0 | Unset, data)

        distances = _parse_distances(d.pop("distances", UNSET))

        def _parse_contours(data: object) -> None | PolygonalChainContoursType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contours_type_0 = PolygonalChainContoursType0.from_dict(data)

                return contours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolygonalChainContoursType0 | Unset, data)

        contours = _parse_contours(d.pop("contours", UNSET))

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

        def _parse_preference(data: object) -> None | PolygonalChainPreferenceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preference_type_0 = check_polygonal_chain_preference_type_0(data)

                return preference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolygonalChainPreferenceType0 | Unset, data)

        preference = _parse_preference(d.pop("preference", UNSET))

        polygonal_chain = cls(
            polygonal_chain_path=polygonal_chain_path,
            markers=markers,
            distances=distances,
            contours=contours,
            label=label,
            note=note,
            style=style,
            key_external=key_external,
            hidden=hidden,
            preference=preference,
        )

        polygonal_chain.additional_properties = d
        return polygonal_chain

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
