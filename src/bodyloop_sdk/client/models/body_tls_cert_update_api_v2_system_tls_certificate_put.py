from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="BodyTlsCertUpdateApiV2SystemTlsCertificatePut")


@_attrs_define
class BodyTlsCertUpdateApiV2SystemTlsCertificatePut:
    cert_file: File
    key_file: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_file = self.cert_file.to_tuple()

        key_file = self.key_file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cert_file": cert_file,
                "key_file": key_file,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("cert_file", self.cert_file.to_tuple()))

        files.append(("key_file", self.key_file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert_file = File(payload=BytesIO(d.pop("cert_file")))

        key_file = File(payload=BytesIO(d.pop("key_file")))

        body_tls_cert_update_api_v2_system_tls_certificate_put = cls(
            cert_file=cert_file,
            key_file=key_file,
        )

        body_tls_cert_update_api_v2_system_tls_certificate_put.additional_properties = d
        return body_tls_cert_update_api_v2_system_tls_certificate_put

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
