from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_geometry_type_0 import ImagesGeometryType0
    from ..models.images_texture_type_0 import ImagesTextureType0


T = TypeVar("T", bound="Images")


@_attrs_define
class Images:
    """Represents images of various categorys"""

    geometry: ImagesGeometryType0 | None | Unset = UNSET
    texture: ImagesTextureType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.images_geometry_type_0 import ImagesGeometryType0
        from ..models.images_texture_type_0 import ImagesTextureType0

        geometry: dict[str, Any] | None | Unset
        if isinstance(self.geometry, Unset):
            geometry = UNSET
        elif isinstance(self.geometry, ImagesGeometryType0):
            geometry = self.geometry.to_dict()
        else:
            geometry = self.geometry

        texture: dict[str, Any] | None | Unset
        if isinstance(self.texture, Unset):
            texture = UNSET
        elif isinstance(self.texture, ImagesTextureType0):
            texture = self.texture.to_dict()
        else:
            texture = self.texture

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if texture is not UNSET:
            field_dict["texture"] = texture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images_geometry_type_0 import ImagesGeometryType0
        from ..models.images_texture_type_0 import ImagesTextureType0

        d = dict(src_dict)

        def _parse_geometry(data: object) -> ImagesGeometryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geometry_type_0 = ImagesGeometryType0.from_dict(data)

                return geometry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImagesGeometryType0 | None | Unset, data)

        geometry = _parse_geometry(d.pop("geometry", UNSET))

        def _parse_texture(data: object) -> ImagesTextureType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                texture_type_0 = ImagesTextureType0.from_dict(data)

                return texture_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImagesTextureType0 | None | Unset, data)

        texture = _parse_texture(d.pop("texture", UNSET))

        images = cls(
            geometry=geometry,
            texture=texture,
        )

        images.additional_properties = d
        return images

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
