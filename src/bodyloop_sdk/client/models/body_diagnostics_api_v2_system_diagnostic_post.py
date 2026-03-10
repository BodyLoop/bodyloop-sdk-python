from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyDiagnosticsApiV2SystemDiagnosticPost")


@_attrs_define
class BodyDiagnosticsApiV2SystemDiagnosticPost:
    viatar_log_start_id: int | None | Unset = UNSET
    viatar_log_limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        viatar_log_start_id: int | None | Unset
        if isinstance(self.viatar_log_start_id, Unset):
            viatar_log_start_id = UNSET
        else:
            viatar_log_start_id = self.viatar_log_start_id

        viatar_log_limit: int | None | Unset
        if isinstance(self.viatar_log_limit, Unset):
            viatar_log_limit = UNSET
        else:
            viatar_log_limit = self.viatar_log_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if viatar_log_start_id is not UNSET:
            field_dict["viatar_log_start_id"] = viatar_log_start_id
        if viatar_log_limit is not UNSET:
            field_dict["viatar_log_limit"] = viatar_log_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_viatar_log_start_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        viatar_log_start_id = _parse_viatar_log_start_id(d.pop("viatar_log_start_id", UNSET))

        def _parse_viatar_log_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        viatar_log_limit = _parse_viatar_log_limit(d.pop("viatar_log_limit", UNSET))

        body_diagnostics_api_v2_system_diagnostic_post = cls(
            viatar_log_start_id=viatar_log_start_id,
            viatar_log_limit=viatar_log_limit,
        )

        body_diagnostics_api_v2_system_diagnostic_post.additional_properties = d
        return body_diagnostics_api_v2_system_diagnostic_post

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
