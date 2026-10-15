from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marker import Marker


T = TypeVar("T", bound="CrosssectionDetailDetails")


@_attrs_define
class CrosssectionDetailDetails:
    additional_properties: dict[str, list[Marker] | Marker] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.marker import Marker  # noqa: PLC0415

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, Marker):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = []
                for additional_property_type_1_item_data in prop:
                    additional_property_type_1_item = additional_property_type_1_item_data.to_dict()
                    field_dict[prop_name].append(additional_property_type_1_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marker import Marker  # noqa: PLC0415

        d = dict(src_dict)
        crosssection_detail_details = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> list[Marker] | Marker:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = Marker.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, list):
                    raise TypeError()
                additional_property_type_1 = []
                _additional_property_type_1 = data
                for additional_property_type_1_item_data in _additional_property_type_1:
                    additional_property_type_1_item = Marker.from_dict(additional_property_type_1_item_data)

                    additional_property_type_1.append(additional_property_type_1_item)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        crosssection_detail_details.additional_properties = additional_properties
        return crosssection_detail_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[Marker] | Marker:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[Marker] | Marker) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
