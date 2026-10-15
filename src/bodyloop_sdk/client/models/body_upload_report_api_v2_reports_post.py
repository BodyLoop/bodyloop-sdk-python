from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadReportApiV2ReportsPost")


@_attrs_define
class BodyUploadReportApiV2ReportsPost:
    file: File
    viatars: list[int] | Unset = UNSET
    probands: list[int] | Unset = UNSET
    label: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        viatars: list[int] | Unset = UNSET
        if not isinstance(self.viatars, Unset):
            viatars = self.viatars

        probands: list[int] | Unset = UNSET
        if not isinstance(self.probands, Unset):
            probands = self.probands

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if viatars is not UNSET:
            field_dict["viatars"] = viatars
        if probands is not UNSET:
            field_dict["probands"] = probands
        if label is not UNSET:
            field_dict["label"] = label
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.viatars, Unset):
            for viatars_item_element in self.viatars:
                files.append(("viatars", (None, str(viatars_item_element).encode(), "text/plain")))

        if not isinstance(self.probands, Unset):
            for probands_item_element in self.probands:
                files.append(("probands", (None, str(probands_item_element).encode(), "text/plain")))

        if not isinstance(self.label, Unset):
            if isinstance(self.label, str):
                files.append(("label", (None, str(self.label).encode(), "text/plain")))
            else:
                files.append(("label", (None, str(self.label).encode(), "text/plain")))

        if not isinstance(self.note, Unset):
            if isinstance(self.note, str):
                files.append(("note", (None, str(self.note).encode(), "text/plain")))
            else:
                files.append(("note", (None, str(self.note).encode(), "text/plain")))

        if not isinstance(self.key_external, Unset):
            if isinstance(self.key_external, str):
                files.append(("key_external", (None, str(self.key_external).encode(), "text/plain")))
            else:
                files.append(("key_external", (None, str(self.key_external).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        viatars = cast(list[int], d.pop("viatars", UNSET))

        probands = cast(list[int], d.pop("probands", UNSET))

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

        body_upload_report_api_v2_reports_post = cls(
            file=file,
            viatars=viatars,
            probands=probands,
            label=label,
            note=note,
            key_external=key_external,
        )

        body_upload_report_api_v2_reports_post.additional_properties = d
        return body_upload_report_api_v2_reports_post

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
