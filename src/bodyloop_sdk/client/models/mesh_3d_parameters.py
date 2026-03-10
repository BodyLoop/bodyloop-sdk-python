from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mesh_3d_parameters_detail_type_0 import (
    Mesh3DParametersDetailType0,
    check_mesh_3d_parameters_detail_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="Mesh3DParameters")


@_attrs_define
class Mesh3DParameters:
    """Parameters influencing the target Mesh3D"""

    detail: Mesh3DParametersDetailType0 | None | Unset = UNSET
    texture: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        elif isinstance(self.detail, str):
            detail = self.detail
        else:
            detail = self.detail

        texture: bool | None | Unset
        if isinstance(self.texture, Unset):
            texture = UNSET
        else:
            texture = self.texture

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if texture is not UNSET:
            field_dict["texture"] = texture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_detail(data: object) -> Mesh3DParametersDetailType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                detail_type_0 = check_mesh_3d_parameters_detail_type_0(data)

                return detail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Mesh3DParametersDetailType0 | None | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_texture(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        texture = _parse_texture(d.pop("texture", UNSET))

        mesh_3d_parameters = cls(
            detail=detail,
            texture=texture,
        )

        mesh_3d_parameters.additional_properties = d
        return mesh_3d_parameters

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
