from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crosssection_areas_type_0 import CrosssectionAreasType0
    from ..models.crosssection_circumferences_type_0 import CrosssectionCircumferencesType0
    from ..models.crosssection_contours_type_0 import CrosssectionContoursType0
    from ..models.crosssection_skeleton_position_type_0 import CrosssectionSkeletonPositionType0


T = TypeVar("T", bound="Crosssection")


@_attrs_define
class Crosssection:
    """Crosssection representation at one marker

    Example:
        {'at_marker': 'marker_a', 'crosssection_path': 'custom.path.M', 'hidden': False, 'key_external': '', 'label':
            'Descriptive label', 'note': 'Meaningful description...'}

    """

    crosssection_path: str | Unset = UNSET
    label: None | str | Unset = UNSET
    at_marker: str | Unset = UNSET
    circumferences: CrosssectionCircumferencesType0 | None | Unset = UNSET
    areas: CrosssectionAreasType0 | None | Unset = UNSET
    contours: CrosssectionContoursType0 | None | Unset = UNSET
    skeleton_position: CrosssectionSkeletonPositionType0 | None | Unset = UNSET
    note: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    preference: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.crosssection_areas_type_0 import CrosssectionAreasType0
        from ..models.crosssection_circumferences_type_0 import CrosssectionCircumferencesType0
        from ..models.crosssection_contours_type_0 import CrosssectionContoursType0
        from ..models.crosssection_skeleton_position_type_0 import CrosssectionSkeletonPositionType0

        crosssection_path = self.crosssection_path

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        at_marker = self.at_marker

        circumferences: dict[str, Any] | None | Unset
        if isinstance(self.circumferences, Unset):
            circumferences = UNSET
        elif isinstance(self.circumferences, CrosssectionCircumferencesType0):
            circumferences = self.circumferences.to_dict()
        else:
            circumferences = self.circumferences

        areas: dict[str, Any] | None | Unset
        if isinstance(self.areas, Unset):
            areas = UNSET
        elif isinstance(self.areas, CrosssectionAreasType0):
            areas = self.areas.to_dict()
        else:
            areas = self.areas

        contours: dict[str, Any] | None | Unset
        if isinstance(self.contours, Unset):
            contours = UNSET
        elif isinstance(self.contours, CrosssectionContoursType0):
            contours = self.contours.to_dict()
        else:
            contours = self.contours

        skeleton_position: dict[str, Any] | None | Unset
        if isinstance(self.skeleton_position, Unset):
            skeleton_position = UNSET
        elif isinstance(self.skeleton_position, CrosssectionSkeletonPositionType0):
            skeleton_position = self.skeleton_position.to_dict()
        else:
            skeleton_position = self.skeleton_position

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
        if crosssection_path is not UNSET:
            field_dict["crosssection_path"] = crosssection_path
        if label is not UNSET:
            field_dict["label"] = label
        if at_marker is not UNSET:
            field_dict["at_marker"] = at_marker
        if circumferences is not UNSET:
            field_dict["circumferences"] = circumferences
        if areas is not UNSET:
            field_dict["areas"] = areas
        if contours is not UNSET:
            field_dict["contours"] = contours
        if skeleton_position is not UNSET:
            field_dict["skeletonPosition"] = skeleton_position
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
        from ..models.crosssection_areas_type_0 import CrosssectionAreasType0
        from ..models.crosssection_circumferences_type_0 import CrosssectionCircumferencesType0
        from ..models.crosssection_contours_type_0 import CrosssectionContoursType0
        from ..models.crosssection_skeleton_position_type_0 import CrosssectionSkeletonPositionType0

        d = dict(src_dict)
        crosssection_path = d.pop("crosssection_path", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        at_marker = d.pop("at_marker", UNSET)

        def _parse_circumferences(data: object) -> CrosssectionCircumferencesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                circumferences_type_0 = CrosssectionCircumferencesType0.from_dict(data)

                return circumferences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CrosssectionCircumferencesType0 | None | Unset, data)

        circumferences = _parse_circumferences(d.pop("circumferences", UNSET))

        def _parse_areas(data: object) -> CrosssectionAreasType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                areas_type_0 = CrosssectionAreasType0.from_dict(data)

                return areas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CrosssectionAreasType0 | None | Unset, data)

        areas = _parse_areas(d.pop("areas", UNSET))

        def _parse_contours(data: object) -> CrosssectionContoursType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contours_type_0 = CrosssectionContoursType0.from_dict(data)

                return contours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CrosssectionContoursType0 | None | Unset, data)

        contours = _parse_contours(d.pop("contours", UNSET))

        def _parse_skeleton_position(data: object) -> CrosssectionSkeletonPositionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                skeleton_position_type_0 = CrosssectionSkeletonPositionType0.from_dict(data)

                return skeleton_position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CrosssectionSkeletonPositionType0 | None | Unset, data)

        skeleton_position = _parse_skeleton_position(d.pop("skeletonPosition", UNSET))

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

        crosssection = cls(
            crosssection_path=crosssection_path,
            label=label,
            at_marker=at_marker,
            circumferences=circumferences,
            areas=areas,
            contours=contours,
            skeleton_position=skeleton_position,
            note=note,
            style=style,
            key_external=key_external,
            hidden=hidden,
            preference=preference,
        )

        crosssection.additional_properties = d
        return crosssection

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
