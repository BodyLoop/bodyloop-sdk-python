from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta import Meta


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """Extended version of `ReportData` that includes unique report_id and meta information."""

    report_type: Literal["viatar"]
    report_id: int
    probands: list[int] | Unset = UNSET
    viatars: list[int] | Unset = UNSET
    filepath: str | Unset = UNSET
    proband_note: None | str | Unset = UNSET
    name_given: None | str | Unset = UNSET
    name_family: None | str | Unset = UNSET
    date_of_birth: None | str | Unset = UNSET
    gender: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    viatar_note: None | str | Unset = UNSET
    scan_timestamp: datetime.datetime | None | Unset = UNSET
    properties: list[Any] | Unset = UNSET
    heights: list[Any] | Unset = UNSET
    distances: list[Any] | Unset = UNSET
    crosssections: list[Any] | Unset = UNSET
    angles: list[Any] | Unset = UNSET
    axes: list[Any] | Unset = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta

        report_type = self.report_type

        report_id = self.report_id

        probands: list[int] | Unset = UNSET
        if not isinstance(self.probands, Unset):
            probands = self.probands

        viatars: list[int] | Unset = UNSET
        if not isinstance(self.viatars, Unset):
            viatars = self.viatars

        filepath = self.filepath

        proband_note: None | str | Unset
        if isinstance(self.proband_note, Unset):
            proband_note = UNSET
        else:
            proband_note = self.proband_note

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
        else:
            date_of_birth = self.date_of_birth

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        viatar_note: None | str | Unset
        if isinstance(self.viatar_note, Unset):
            viatar_note = UNSET
        else:
            viatar_note = self.viatar_note

        scan_timestamp: None | str | Unset
        if isinstance(self.scan_timestamp, Unset):
            scan_timestamp = UNSET
        elif isinstance(self.scan_timestamp, datetime.datetime):
            scan_timestamp = self.scan_timestamp.isoformat()
        else:
            scan_timestamp = self.scan_timestamp

        properties: list[Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties

        heights: list[Any] | Unset = UNSET
        if not isinstance(self.heights, Unset):
            heights = self.heights

        distances: list[Any] | Unset = UNSET
        if not isinstance(self.distances, Unset):
            distances = self.distances

        crosssections: list[Any] | Unset = UNSET
        if not isinstance(self.crosssections, Unset):
            crosssections = self.crosssections

        angles: list[Any] | Unset = UNSET
        if not isinstance(self.angles, Unset):
            angles = self.angles

        axes: list[Any] | Unset = UNSET
        if not isinstance(self.axes, Unset):
            axes = self.axes

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
                "report_type": report_type,
                "report_id": report_id,
            }
        )
        if probands is not UNSET:
            field_dict["probands"] = probands
        if viatars is not UNSET:
            field_dict["viatars"] = viatars
        if filepath is not UNSET:
            field_dict["filepath"] = filepath
        if proband_note is not UNSET:
            field_dict["proband_note"] = proband_note
        if name_given is not UNSET:
            field_dict["name_given"] = name_given
        if name_family is not UNSET:
            field_dict["name_family"] = name_family
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if address is not UNSET:
            field_dict["address"] = address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if model is not UNSET:
            field_dict["model"] = model
        if viatar_note is not UNSET:
            field_dict["viatar_note"] = viatar_note
        if scan_timestamp is not UNSET:
            field_dict["scan_timestamp"] = scan_timestamp
        if properties is not UNSET:
            field_dict["properties"] = properties
        if heights is not UNSET:
            field_dict["heights"] = heights
        if distances is not UNSET:
            field_dict["distances"] = distances
        if crosssections is not UNSET:
            field_dict["crosssections"] = crosssections
        if angles is not UNSET:
            field_dict["angles"] = angles
        if axes is not UNSET:
            field_dict["axes"] = axes
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta import Meta

        d = dict(src_dict)
        report_type = cast(Literal["viatar"], d.pop("report_type"))
        if report_type != "viatar":
            raise ValueError(f"report_type must match const 'viatar', got '{report_type}'")

        report_id = d.pop("report_id")

        probands = cast(list[int], d.pop("probands", UNSET))

        viatars = cast(list[int], d.pop("viatars", UNSET))

        filepath = d.pop("filepath", UNSET)

        def _parse_proband_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proband_note = _parse_proband_note(d.pop("proband_note", UNSET))

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

        def _parse_date_of_birth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_viatar_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        viatar_note = _parse_viatar_note(d.pop("viatar_note", UNSET))

        def _parse_scan_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scan_timestamp_type_0 = isoparse(data)

                return scan_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scan_timestamp = _parse_scan_timestamp(d.pop("scan_timestamp", UNSET))

        properties = cast(list[Any], d.pop("properties", UNSET))

        heights = cast(list[Any], d.pop("heights", UNSET))

        distances = cast(list[Any], d.pop("distances", UNSET))

        crosssections = cast(list[Any], d.pop("crosssections", UNSET))

        angles = cast(list[Any], d.pop("angles", UNSET))

        axes = cast(list[Any], d.pop("axes", UNSET))

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

        report = cls(
            report_type=report_type,
            report_id=report_id,
            probands=probands,
            viatars=viatars,
            filepath=filepath,
            proband_note=proband_note,
            name_given=name_given,
            name_family=name_family,
            date_of_birth=date_of_birth,
            gender=gender,
            address=address,
            phone=phone,
            email=email,
            model=model,
            viatar_note=viatar_note,
            scan_timestamp=scan_timestamp,
            properties=properties,
            heights=heights,
            distances=distances,
            crosssections=crosssections,
            angles=angles,
            axes=axes,
            meta=meta,
        )

        report.additional_properties = d
        return report

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
