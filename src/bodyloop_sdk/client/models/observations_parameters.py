from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observation_model import ObservationModel


T = TypeVar("T", bound="ObservationsParameters")


@_attrs_define
class ObservationsParameters:
    """Parameters influencing Observations"""

    weight: ObservationModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observation_model import ObservationModel  # noqa: PLC0415

        d = dict(src_dict)
        _weight = d.pop("weight", UNSET)
        weight: ObservationModel | Unset
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = ObservationModel.from_dict(_weight)

        observations_parameters = cls(
            weight=weight,
        )

        observations_parameters.additional_properties = d
        return observations_parameters

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
