from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.avatar_3d_parameters_output_clothing_type_0 import (
    Avatar3DParametersOutputClothingType0,
    check_avatar_3d_parameters_output_clothing_type_0,
)
from ..models.avatar_3d_parameters_output_model_type_0 import (
    Avatar3DParametersOutputModelType0,
    check_avatar_3d_parameters_output_model_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="Avatar3DParametersOutput")


@_attrs_define
class Avatar3DParametersOutput:
    """Parameters influencing the target Avatar3D"""

    model: Avatar3DParametersOutputModelType0 | None | Unset = UNSET
    clothing: Avatar3DParametersOutputClothingType0 | None | Unset = UNSET
    reverse: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, str):
            model = self.model
        else:
            model = self.model

        clothing: None | str | Unset
        if isinstance(self.clothing, Unset):
            clothing = UNSET
        elif isinstance(self.clothing, str):
            clothing = self.clothing
        else:
            clothing = self.clothing

        reverse: bool | None | Unset
        if isinstance(self.reverse, Unset):
            reverse = UNSET
        else:
            reverse = self.reverse

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if clothing is not UNSET:
            field_dict["clothing"] = clothing
        if reverse is not UNSET:
            field_dict["reverse"] = reverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_model(data: object) -> Avatar3DParametersOutputModelType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_0 = check_avatar_3d_parameters_output_model_type_0(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Avatar3DParametersOutputModelType0 | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_clothing(data: object) -> Avatar3DParametersOutputClothingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clothing_type_0 = check_avatar_3d_parameters_output_clothing_type_0(data)

                return clothing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Avatar3DParametersOutputClothingType0 | None | Unset, data)

        clothing = _parse_clothing(d.pop("clothing", UNSET))

        def _parse_reverse(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reverse = _parse_reverse(d.pop("reverse", UNSET))

        avatar_3d_parameters_output = cls(
            model=model,
            clothing=clothing,
            reverse=reverse,
        )

        avatar_3d_parameters_output.additional_properties = d
        return avatar_3d_parameters_output

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
