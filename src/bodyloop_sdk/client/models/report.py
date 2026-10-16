from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_report_type import ReportReportType, check_report_report_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta import Meta


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    report_type: ReportReportType
    report_id: int
    probands: list[int] | Unset = UNSET
    viatars: list[int] | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta  # noqa: PLC0415

        report_type: str = self.report_type

        report_id = self.report_id

        probands: list[int] | Unset = UNSET
        if not isinstance(self.probands, Unset):
            probands = self.probands

        viatars: list[int] | Unset = UNSET
        if not isinstance(self.viatars, Unset):
            viatars = self.viatars

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

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
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta import Meta  # noqa: PLC0415

        d = dict(src_dict)
        report_type = check_report_report_type(d.pop("report_type"))

        report_id = d.pop("report_id")

        probands = cast(list[int], d.pop("probands", UNSET))

        viatars = cast(list[int], d.pop("viatars", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

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
            label=label,
            note=note,
            key_external=key_external,
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
