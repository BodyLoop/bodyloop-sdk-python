from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost")


@_attrs_define
class BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost:
    geometry: list[str]
    texture: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geometry = self.geometry

        texture = self.texture

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
            files.append(("geometry", (None, str(geometry_item_element).encode(), "text/plain")))

        for texture_item_element in self.texture:
            files.append(("texture", (None, str(texture_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        geometry = cast(list[str], d.pop("geometry"))

        texture = cast(list[str], d.pop("texture"))

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
