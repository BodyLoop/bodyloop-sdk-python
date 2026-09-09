from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.body_test_blink_lights_api_v2_system_lights_blink_post_mode import (
    BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode,
    check_body_test_blink_lights_api_v2_system_lights_blink_post_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyTestBlinkLightsApiV2SystemLightsBlinkPost")


@_attrs_define
class BodyTestBlinkLightsApiV2SystemLightsBlinkPost:
    mode: BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode | Unset = "default"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_body_test_blink_lights_api_v2_system_lights_blink_post_mode(_mode)

        body_test_blink_lights_api_v2_system_lights_blink_post = cls(
            mode=mode,
        )

        body_test_blink_lights_api_v2_system_lights_blink_post.additional_properties = d
        return body_test_blink_lights_api_v2_system_lights_blink_post

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
