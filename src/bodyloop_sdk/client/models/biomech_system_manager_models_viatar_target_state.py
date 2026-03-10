from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.biomech_system_manager_models_viatar_target_state_status_type_0 import (
    BiomechSystemManagerModelsViatarTargetStateStatusType0,
    check_biomech_system_manager_models_viatar_target_state_status_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BiomechSystemManagerModelsViatarTargetState")


@_attrs_define
class BiomechSystemManagerModelsViatarTargetState:
    """Represents the state of a Target"""

    status: BiomechSystemManagerModelsViatarTargetStateStatusType0 | None | Unset = UNSET
    progress: float | None | Unset = UNSET
    description: None | str | Unset = UNSET
    notification: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, str):
            status = self.status
        else:
            status = self.status

        progress: float | None | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        notification: list[str] | None | Unset
        if isinstance(self.notification, Unset):
            notification = UNSET
        elif isinstance(self.notification, list):
            notification = self.notification

        else:
            notification = self.notification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if progress is not UNSET:
            field_dict["progress"] = progress
        if description is not UNSET:
            field_dict["description"] = description
        if notification is not UNSET:
            field_dict["notification"] = notification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> BiomechSystemManagerModelsViatarTargetStateStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = check_biomech_system_manager_models_viatar_target_state_status_type_0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BiomechSystemManagerModelsViatarTargetStateStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_progress(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_notification(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_type_0 = cast(list[str], data)

                return notification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notification = _parse_notification(d.pop("notification", UNSET))

        biomech_system_manager_models_viatar_target_state = cls(
            status=status,
            progress=progress,
            description=description,
            notification=notification,
        )

        biomech_system_manager_models_viatar_target_state.additional_properties = d
        return biomech_system_manager_models_viatar_target_state

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
