from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost")


@_attrs_define
class BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost:
    ring_brightness: int | Unset = 40
    proj_brightness: int | Unset = 83
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ring_brightness = self.ring_brightness

        proj_brightness = self.proj_brightness

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ring_brightness is not UNSET:
            field_dict["ring_brightness"] = ring_brightness
        if proj_brightness is not UNSET:
            field_dict["proj_brightness"] = proj_brightness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ring_brightness = d.pop("ring_brightness", UNSET)

        proj_brightness = d.pop("proj_brightness", UNSET)

        body_capture_camera_image_api_v2_system_cameras_camera_capture_post = cls(
            ring_brightness=ring_brightness,
            proj_brightness=proj_brightness,
        )

        body_capture_camera_image_api_v2_system_cameras_camera_capture_post.additional_properties = d
        return body_capture_camera_image_api_v2_system_cameras_camera_capture_post

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
