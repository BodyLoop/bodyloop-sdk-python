from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost")


@_attrs_define
class BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost:
    geometry: list[File]
    texture: list[File]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geometry = []
        for geometry_item_data in self.geometry:
            geometry_item = geometry_item_data.to_tuple()

            geometry.append(geometry_item)

        texture = []
        for texture_item_data in self.texture:
            texture_item = texture_item_data.to_tuple()

            texture.append(texture_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "geometry": geometry,
                "texture": texture,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        for geometry_item_element in self.geometry:
            files.append(("geometry", geometry_item_element.to_tuple()))

        for texture_item_element in self.texture:
            files.append(("texture", texture_item_element.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        geometry = []
        _geometry = d.pop("geometry")
        for geometry_item_data in _geometry:
            geometry_item = File(payload=BytesIO(geometry_item_data))

            geometry.append(geometry_item)

        texture = []
        _texture = d.pop("texture")
        for texture_item_data in _texture:
            texture_item = File(payload=BytesIO(texture_item_data))

            texture.append(texture_item)

        body_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post = cls(
            geometry=geometry,
            texture=texture,
        )

        body_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post.additional_properties = d
        return body_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post

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
