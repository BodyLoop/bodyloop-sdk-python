from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.body_patch_update_stream_api_v2_system_update_update_stream_patch_update_stream import (
    BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream,
    check_body_patch_update_stream_api_v2_system_update_update_stream_patch_update_stream,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch")


@_attrs_define
class BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch:
    update_stream: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_stream: str | Unset = UNSET
        if not isinstance(self.update_stream, Unset):
            update_stream = self.update_stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_stream is not UNSET:
            field_dict["update_stream"] = update_stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _update_stream = d.pop("update_stream", UNSET)
        update_stream: BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream | Unset
        if isinstance(_update_stream, Unset):
            update_stream = UNSET
        else:
            update_stream = check_body_patch_update_stream_api_v2_system_update_update_stream_patch_update_stream(
                _update_stream
            )

        body_patch_update_stream_api_v2_system_update_update_stream_patch = cls(
            update_stream=update_stream,
        )

        body_patch_update_stream_api_v2_system_update_update_stream_patch.additional_properties = d
        return body_patch_update_stream_api_v2_system_update_update_stream_patch

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
