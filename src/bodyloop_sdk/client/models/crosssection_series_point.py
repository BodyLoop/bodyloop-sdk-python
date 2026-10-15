from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrosssectionSeriesPoint")


@_attrs_define
class CrosssectionSeriesPoint:
    """One data point of a crosssection series (see `ViatarDataSeries`)"""

    distance_from_root: float | None | Unset = UNSET
    circumference: float | None | Unset = UNSET
    area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distance_from_root: float | None | Unset
        if isinstance(self.distance_from_root, Unset):
            distance_from_root = UNSET
        else:
            distance_from_root = self.distance_from_root

        circumference: float | None | Unset
        if isinstance(self.circumference, Unset):
            circumference = UNSET
        else:
            circumference = self.circumference

        area: float | None | Unset
        if isinstance(self.area, Unset):
            area = UNSET
        else:
            area = self.area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance_from_root is not UNSET:
            field_dict["distanceFromRoot"] = distance_from_root
        if circumference is not UNSET:
            field_dict["circumference"] = circumference
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_distance_from_root(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_from_root = _parse_distance_from_root(d.pop("distanceFromRoot", UNSET))

        def _parse_circumference(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        circumference = _parse_circumference(d.pop("circumference", UNSET))

        def _parse_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area = _parse_area(d.pop("area", UNSET))

        crosssection_series_point = cls(
            distance_from_root=distance_from_root,
            circumference=circumference,
            area=area,
        )

        crosssection_series_point.additional_properties = d
        return crosssection_series_point

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
