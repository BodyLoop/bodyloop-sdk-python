from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost")


@_attrs_define
class BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost:
    target_kind: Literal["init"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_kind = self.target_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_kind": target_kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_kind = cast(Literal["init"], d.pop("target_kind"))
        if target_kind != "init":
            raise ValueError(f"target_kind must match const 'init', got '{target_kind}'")

        body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post = cls(
            target_kind=target_kind,
        )

        body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post.additional_properties = d
        return body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post

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
