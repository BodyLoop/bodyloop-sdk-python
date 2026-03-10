from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.contact import Contact
    from ..models.meta import Meta
    from ..models.upload_credentials import UploadCredentials


T = TypeVar("T", bound="Proband")


@_attrs_define
class Proband:
    """Extended version of `ProbandData` that includes unique proband_id and meta information.

    Example:
        {'address': {'city': 'Stuttgart', 'country': 'Germany', 'street': 'Hauptstraße 20', 'zip_code': '70173'},
            'contact': {'email': 'sophie.neumann@example.de', 'phone': '+49-711-12345678'}, 'date_of_birth': '1994-06-18',
            'gender': 'female', 'key_external': 'ATH11223', 'name_family': 'Neumann', 'name_given': 'Sophie', 'note':
            'Früherer Kreuzbandriss'}

    """

    proband_id: int
    name_given: None | str | Unset = UNSET
    name_family: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    gender: None | str | Unset = UNSET
    contact: Contact | None | Unset = UNSET
    address: Address | None | Unset = UNSET
    note: None | str | Unset = UNSET
    sub: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    upload_credentials: None | Unset | UploadCredentials = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address import Address
        from ..models.contact import Contact
        from ..models.meta import Meta
        from ..models.upload_credentials import UploadCredentials

        proband_id = self.proband_id

        name_given: None | str | Unset
        if isinstance(self.name_given, Unset):
            name_given = UNSET
        else:
            name_given = self.name_given

        name_family: None | str | Unset
        if isinstance(self.name_family, Unset):
            name_family = UNSET
        else:
            name_family = self.name_family

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        contact: dict[str, Any] | None | Unset
        if isinstance(self.contact, Unset):
            contact = UNSET
        elif isinstance(self.contact, Contact):
            contact = self.contact.to_dict()
        else:
            contact = self.contact

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, Address):
            address = self.address.to_dict()
        else:
            address = self.address

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        sub: None | str | Unset
        if isinstance(self.sub, Unset):
            sub = UNSET
        else:
            sub = self.sub

        key_external: None | str | Unset
        if isinstance(self.key_external, Unset):
            key_external = UNSET
        else:
            key_external = self.key_external

        upload_credentials: dict[str, Any] | None | Unset
        if isinstance(self.upload_credentials, Unset):
            upload_credentials = UNSET
        elif isinstance(self.upload_credentials, UploadCredentials):
            upload_credentials = self.upload_credentials.to_dict()
        else:
            upload_credentials = self.upload_credentials

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, Meta):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proband_id": proband_id,
            }
        )
        if name_given is not UNSET:
            field_dict["name_given"] = name_given
        if name_family is not UNSET:
            field_dict["name_family"] = name_family
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if contact is not UNSET:
            field_dict["contact"] = contact
        if address is not UNSET:
            field_dict["address"] = address
        if note is not UNSET:
            field_dict["note"] = note
        if sub is not UNSET:
            field_dict["sub"] = sub
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if upload_credentials is not UNSET:
            field_dict["upload_credentials"] = upload_credentials
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.contact import Contact
        from ..models.meta import Meta
        from ..models.upload_credentials import UploadCredentials

        d = dict(src_dict)
        proband_id = d.pop("proband_id")

        def _parse_name_given(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_given = _parse_name_given(d.pop("name_given", UNSET))

        def _parse_name_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_family = _parse_name_family(d.pop("name_family", UNSET))

        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = isoparse(data).date()

                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_contact(data: object) -> Contact | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contact_type_0 = Contact.from_dict(data)

                return contact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Contact | None | Unset, data)

        contact = _parse_contact(d.pop("contact", UNSET))

        def _parse_address(data: object) -> Address | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = Address.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Address | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_sub(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub = _parse_sub(d.pop("sub", UNSET))

        def _parse_key_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_external = _parse_key_external(d.pop("key_external", UNSET))

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

        def _parse_meta(data: object) -> Meta | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = Meta.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Meta | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        proband = cls(
            proband_id=proband_id,
            name_given=name_given,
            name_family=name_family,
            date_of_birth=date_of_birth,
            gender=gender,
            contact=contact,
            address=address,
            note=note,
            sub=sub,
            key_external=key_external,
            upload_credentials=upload_credentials,
            meta=meta,
        )

        proband.additional_properties = d
        return proband

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
