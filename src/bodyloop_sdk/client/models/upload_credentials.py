from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upload_credentials_method_type_0 import (
    UploadCredentialsMethodType0,
    check_upload_credentials_method_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_credentials_headers_type_0 import UploadCredentialsHeadersType0


T = TypeVar("T", bound="UploadCredentials")


@_attrs_define
class UploadCredentials:
    """Upload Credentials"""

    method: None | Unset | UploadCredentialsMethodType0 = UNSET
    url: None | str | Unset = UNSET
    auth: list[str] | None | Unset = UNSET
    headers: None | Unset | UploadCredentialsHeadersType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_credentials_headers_type_0 import UploadCredentialsHeadersType0

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        elif isinstance(self.method, str):
            method = self.method
        else:
            method = self.method

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        auth: list[str] | None | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, list):
            auth = []
            for auth_type_0_item_data in self.auth:
                auth_type_0_item: str
                auth_type_0_item = auth_type_0_item_data
                auth.append(auth_type_0_item)

        else:
            auth = self.auth

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, UploadCredentialsHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url
        if auth is not UNSET:
            field_dict["auth"] = auth
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_credentials_headers_type_0 import UploadCredentialsHeadersType0

        d = dict(src_dict)

        def _parse_method(data: object) -> None | Unset | UploadCredentialsMethodType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_type_0 = check_upload_credentials_method_type_0(data)

                return method_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UploadCredentialsMethodType0, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_auth(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auth_type_0 = []
                _auth_type_0 = data
                for auth_type_0_item_data in _auth_type_0:

                    def _parse_auth_type_0_item(data: object) -> str:
                        return cast(str, data)

                    auth_type_0_item = _parse_auth_type_0_item(auth_type_0_item_data)

                    auth_type_0.append(auth_type_0_item)

                return auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        auth = _parse_auth(d.pop("auth", UNSET))

        def _parse_headers(data: object) -> None | Unset | UploadCredentialsHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = UploadCredentialsHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UploadCredentialsHeadersType0, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        upload_credentials = cls(
            method=method,
            url=url,
            auth=auth,
            headers=headers,
        )

        upload_credentials.additional_properties = d
        return upload_credentials

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
