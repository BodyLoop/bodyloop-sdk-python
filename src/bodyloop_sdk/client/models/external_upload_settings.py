from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_credentials import UploadCredentials


T = TypeVar("T", bound="ExternalUploadSettings")


@_attrs_define
class ExternalUploadSettings:
    """Settings for external upload"""

    upload_credentials: None | Unset | UploadCredentials = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_credentials import UploadCredentials

        upload_credentials: dict[str, Any] | None | Unset
        if isinstance(self.upload_credentials, Unset):
            upload_credentials = UNSET
        elif isinstance(self.upload_credentials, UploadCredentials):
            upload_credentials = self.upload_credentials.to_dict()
        else:
            upload_credentials = self.upload_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_credentials is not UNSET:
            field_dict["upload_credentials"] = upload_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_credentials import UploadCredentials

        d = dict(src_dict)

        def _parse_upload_credentials(data: object) -> None | Unset | UploadCredentials:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upload_credentials_type_0 = UploadCredentials.from_dict(data)

                return upload_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UploadCredentials, data)

        upload_credentials = _parse_upload_credentials(d.pop("upload_credentials", UNSET))

        external_upload_settings = cls(
            upload_credentials=upload_credentials,
        )

        external_upload_settings.additional_properties = d
        return external_upload_settings

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
