from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_recreate_target_kind_type_0 import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0,
    check_body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_recreate_target_kind_type_0,
)
from ..models.body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_target_kind import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind,
    check_body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_target_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost")


@_attrs_define
class BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost:
    target_kind: BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind
    recreate_target_kind: (
        BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_kind: str = self.target_kind

        recreate_target_kind: None | str | Unset
        if isinstance(self.recreate_target_kind, Unset):
            recreate_target_kind = UNSET
        elif isinstance(self.recreate_target_kind, str):
            recreate_target_kind = self.recreate_target_kind
        else:
            recreate_target_kind = self.recreate_target_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_kind": target_kind,
            }
        )
        if recreate_target_kind is not UNSET:
            field_dict["recreate_target_kind"] = recreate_target_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_kind = (
            check_body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_target_kind(
                d.pop("target_kind")
            )
        )

        def _parse_recreate_target_kind(
            data: object,
        ) -> (
            BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recreate_target_kind_type_0 = check_body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_recreate_target_kind_type_0(
                    data
                )

                return recreate_target_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0
                | None
                | Unset,
                data,
            )

        recreate_target_kind = _parse_recreate_target_kind(d.pop("recreate_target_kind", UNSET))

        body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post = cls(
            target_kind=target_kind,
            recreate_target_kind=recreate_target_kind,
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
