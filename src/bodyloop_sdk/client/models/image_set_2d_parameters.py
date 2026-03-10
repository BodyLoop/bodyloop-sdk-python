from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageSet2DParameters")


@_attrs_define
class ImageSet2DParameters:
    """Parameters influencing the target ImageSet2D"""

    exposure_time: int | None | Unset = UNSET
    projector_brightness: int | None | Unset = UNSET
    ring_brightness: int | None | Unset = UNSET
    keep_images: bool | None | Unset = UNSET
    mass_from_phd: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exposure_time: int | None | Unset
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        projector_brightness: int | None | Unset
        if isinstance(self.projector_brightness, Unset):
            projector_brightness = UNSET
        else:
            projector_brightness = self.projector_brightness

        ring_brightness: int | None | Unset
        if isinstance(self.ring_brightness, Unset):
            ring_brightness = UNSET
        else:
            ring_brightness = self.ring_brightness

        keep_images: bool | None | Unset
        if isinstance(self.keep_images, Unset):
            keep_images = UNSET
        else:
            keep_images = self.keep_images

        mass_from_phd: bool | None | Unset
        if isinstance(self.mass_from_phd, Unset):
            mass_from_phd = UNSET
        else:
            mass_from_phd = self.mass_from_phd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exposure_time is not UNSET:
            field_dict["exposure_time"] = exposure_time
        if projector_brightness is not UNSET:
            field_dict["projector_brightness"] = projector_brightness
        if ring_brightness is not UNSET:
            field_dict["ring_brightness"] = ring_brightness
        if keep_images is not UNSET:
            field_dict["keep_images"] = keep_images
        if mass_from_phd is not UNSET:
            field_dict["mass_from_phd"] = mass_from_phd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_exposure_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exposure_time = _parse_exposure_time(d.pop("exposure_time", UNSET))

        def _parse_projector_brightness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        projector_brightness = _parse_projector_brightness(d.pop("projector_brightness", UNSET))

        def _parse_ring_brightness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ring_brightness = _parse_ring_brightness(d.pop("ring_brightness", UNSET))

        def _parse_keep_images(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_images = _parse_keep_images(d.pop("keep_images", UNSET))

        def _parse_mass_from_phd(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mass_from_phd = _parse_mass_from_phd(d.pop("mass_from_phd", UNSET))

        image_set_2d_parameters = cls(
            exposure_time=exposure_time,
            projector_brightness=projector_brightness,
            ring_brightness=ring_brightness,
            keep_images=keep_images,
            mass_from_phd=mass_from_phd,
        )

        image_set_2d_parameters.additional_properties = d
        return image_set_2d_parameters

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
