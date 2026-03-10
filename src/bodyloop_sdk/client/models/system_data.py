from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_data_update_stream_type_0 import (
    SystemDataUpdateStreamType0,
    check_system_data_update_stream_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_authentification_settings import ExternalAuthentificationSettings
    from ..models.external_upload_settings import ExternalUploadSettings
    from ..models.system_os_data import SystemOsData


T = TypeVar("T", bound="SystemData")


@_attrs_define
class SystemData:
    """Extended version of `SystemDb` that includes meta information and all read-only settings."""

    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    update_stream: None | SystemDataUpdateStreamType0 | Unset = UNSET
    active_scanner_initialization: int | None | Unset = UNSET
    external_upload: ExternalUploadSettings | None | Unset = UNSET
    external_auth: ExternalAuthentificationSettings | None | Unset = UNSET
    os: None | SystemOsData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_authentification_settings import ExternalAuthentificationSettings
        from ..models.external_upload_settings import ExternalUploadSettings
        from ..models.system_os_data import SystemOsData

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        key_external: None | str | Unset
        if isinstance(self.key_external, Unset):
            key_external = UNSET
        else:
            key_external = self.key_external

        update_stream: None | str | Unset
        if isinstance(self.update_stream, Unset):
            update_stream = UNSET
        elif isinstance(self.update_stream, str):
            update_stream = self.update_stream
        else:
            update_stream = self.update_stream

        active_scanner_initialization: int | None | Unset
        if isinstance(self.active_scanner_initialization, Unset):
            active_scanner_initialization = UNSET
        else:
            active_scanner_initialization = self.active_scanner_initialization

        external_upload: dict[str, Any] | None | Unset
        if isinstance(self.external_upload, Unset):
            external_upload = UNSET
        elif isinstance(self.external_upload, ExternalUploadSettings):
            external_upload = self.external_upload.to_dict()
        else:
            external_upload = self.external_upload

        external_auth: dict[str, Any] | None | Unset
        if isinstance(self.external_auth, Unset):
            external_auth = UNSET
        elif isinstance(self.external_auth, ExternalAuthentificationSettings):
            external_auth = self.external_auth.to_dict()
        else:
            external_auth = self.external_auth

        os: dict[str, Any] | None | Unset
        if isinstance(self.os, Unset):
            os = UNSET
        elif isinstance(self.os, SystemOsData):
            os = self.os.to_dict()
        else:
            os = self.os

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if update_stream is not UNSET:
            field_dict["update_stream"] = update_stream
        if active_scanner_initialization is not UNSET:
            field_dict["active_scanner_initialization"] = active_scanner_initialization
        if external_upload is not UNSET:
            field_dict["external_upload"] = external_upload
        if external_auth is not UNSET:
            field_dict["external_auth"] = external_auth
        if os is not UNSET:
            field_dict["os"] = os

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_authentification_settings import ExternalAuthentificationSettings
        from ..models.external_upload_settings import ExternalUploadSettings
        from ..models.system_os_data import SystemOsData

        d = dict(src_dict)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_key_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_external = _parse_key_external(d.pop("key_external", UNSET))

        def _parse_update_stream(data: object) -> None | SystemDataUpdateStreamType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_stream_type_0 = check_system_data_update_stream_type_0(data)

                return update_stream_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDataUpdateStreamType0 | Unset, data)

        update_stream = _parse_update_stream(d.pop("update_stream", UNSET))

        def _parse_active_scanner_initialization(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_scanner_initialization = _parse_active_scanner_initialization(
            d.pop("active_scanner_initialization", UNSET)
        )

        def _parse_external_upload(data: object) -> ExternalUploadSettings | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_upload_type_0 = ExternalUploadSettings.from_dict(data)

                return external_upload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalUploadSettings | None | Unset, data)

        external_upload = _parse_external_upload(d.pop("external_upload", UNSET))

        def _parse_external_auth(data: object) -> ExternalAuthentificationSettings | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_auth_type_0 = ExternalAuthentificationSettings.from_dict(data)

                return external_auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalAuthentificationSettings | None | Unset, data)

        external_auth = _parse_external_auth(d.pop("external_auth", UNSET))

        def _parse_os(data: object) -> None | SystemOsData | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                os_type_0 = SystemOsData.from_dict(data)

                return os_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemOsData | Unset, data)

        os = _parse_os(d.pop("os", UNSET))

        system_data = cls(
            note=note,
            key_external=key_external,
            update_stream=update_stream,
            active_scanner_initialization=active_scanner_initialization,
            external_upload=external_upload,
            external_auth=external_auth,
            os=os,
        )

        system_data.additional_properties = d
        return system_data

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
