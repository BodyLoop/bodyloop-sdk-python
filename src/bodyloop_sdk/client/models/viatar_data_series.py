from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.viatar_data_series_crosssections_type_0 import ViatarDataSeriesCrosssectionsType0


T = TypeVar("T", bound="ViatarDataSeries")


@_attrs_define
class ViatarDataSeries:
    """Represents measurments of type DataSeries"""

    crosssections: None | Unset | ViatarDataSeriesCrosssectionsType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.viatar_data_series_crosssections_type_0 import ViatarDataSeriesCrosssectionsType0

        crosssections: dict[str, Any] | None | Unset
        if isinstance(self.crosssections, Unset):
            crosssections = UNSET
        elif isinstance(self.crosssections, ViatarDataSeriesCrosssectionsType0):
            crosssections = self.crosssections.to_dict()
        else:
            crosssections = self.crosssections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crosssections is not UNSET:
            field_dict["crosssections"] = crosssections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.viatar_data_series_crosssections_type_0 import ViatarDataSeriesCrosssectionsType0

        d = dict(src_dict)

        def _parse_crosssections(data: object) -> None | Unset | ViatarDataSeriesCrosssectionsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crosssections_type_0 = ViatarDataSeriesCrosssectionsType0.from_dict(data)

                return crosssections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarDataSeriesCrosssectionsType0, data)

        crosssections = _parse_crosssections(d.pop("crosssections", UNSET))

        viatar_data_series = cls(
            crosssections=crosssections,
        )

        viatar_data_series.additional_properties = d
        return viatar_data_series

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
