from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.body_set_event_api_v2_statistic_event_post_event_status_type_0 import (
    BodySetEventApiV2StatisticEventPostEventStatusType0,
    check_body_set_event_api_v2_statistic_event_post_event_status_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodySetEventApiV2StatisticEventPost")


@_attrs_define
class BodySetEventApiV2StatisticEventPost:
    event: str
    event_status: BodySetEventApiV2StatisticEventPostEventStatusType0 | None | Unset = UNSET
    info: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        event_status: None | str | Unset
        if isinstance(self.event_status, Unset):
            event_status = UNSET
        elif isinstance(self.event_status, str):
            event_status = self.event_status
        else:
            event_status = self.event_status

        info: None | str | Unset
        if isinstance(self.info, Unset):
            info = UNSET
        else:
            info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
            }
        )
        if event_status is not UNSET:
            field_dict["event_status"] = event_status
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        def _parse_event_status(data: object) -> BodySetEventApiV2StatisticEventPostEventStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_status_type_0 = check_body_set_event_api_v2_statistic_event_post_event_status_type_0(data)

                return event_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BodySetEventApiV2StatisticEventPostEventStatusType0 | None | Unset, data)

        event_status = _parse_event_status(d.pop("event_status", UNSET))

        def _parse_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        info = _parse_info(d.pop("info", UNSET))

        body_set_event_api_v2_statistic_event_post = cls(
            event=event,
            event_status=event_status,
            info=info,
        )

        body_set_event_api_v2_statistic_event_post.additional_properties = d
        return body_set_event_api_v2_statistic_event_post

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
