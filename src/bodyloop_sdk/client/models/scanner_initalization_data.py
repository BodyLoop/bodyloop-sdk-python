from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scanner_initalization_data_scanner_type_type_0 import (
    ScannerInitalizationDataScannerTypeType0,
    check_scanner_initalization_data_scanner_type_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scanner_initalization_data_targets_type_0 import ScannerInitalizationDataTargetsType0


T = TypeVar("T", bound="ScannerInitalizationData")


@_attrs_define
class ScannerInitalizationData:
    """Summary of ScannerInitalizationData

    Example:
        {'note': 'A default initialization.', 'scanner_type': '4pillar_32cam'}

    """

    targets: None | ScannerInitalizationDataTargetsType0 | Unset = UNSET
    init_directory: None | str | Unset = UNSET
    scanner_type: None | ScannerInitalizationDataScannerTypeType0 | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scanner_initalization_data_targets_type_0 import ScannerInitalizationDataTargetsType0

        targets: dict[str, Any] | None | Unset
        if isinstance(self.targets, Unset):
            targets = UNSET
        elif isinstance(self.targets, ScannerInitalizationDataTargetsType0):
            targets = self.targets.to_dict()
        else:
            targets = self.targets

        init_directory: None | str | Unset
        if isinstance(self.init_directory, Unset):
            init_directory = UNSET
        else:
            init_directory = self.init_directory

        scanner_type: None | str | Unset
        if isinstance(self.scanner_type, Unset):
            scanner_type = UNSET
        elif isinstance(self.scanner_type, str):
            scanner_type = self.scanner_type
        else:
            scanner_type = self.scanner_type

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if targets is not UNSET:
            field_dict["targets"] = targets
        if init_directory is not UNSET:
            field_dict["init_directory"] = init_directory
        if scanner_type is not UNSET:
            field_dict["scanner_type"] = scanner_type
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scanner_initalization_data_targets_type_0 import ScannerInitalizationDataTargetsType0

        d = dict(src_dict)

        def _parse_targets(data: object) -> None | ScannerInitalizationDataTargetsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                targets_type_0 = ScannerInitalizationDataTargetsType0.from_dict(data)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScannerInitalizationDataTargetsType0 | Unset, data)

        targets = _parse_targets(d.pop("targets", UNSET))

        def _parse_init_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        init_directory = _parse_init_directory(d.pop("init_directory", UNSET))

        def _parse_scanner_type(data: object) -> None | ScannerInitalizationDataScannerTypeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scanner_type_type_0 = check_scanner_initalization_data_scanner_type_type_0(data)

                return scanner_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScannerInitalizationDataScannerTypeType0 | Unset, data)

        scanner_type = _parse_scanner_type(d.pop("scanner_type", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        scanner_initalization_data = cls(
            targets=targets,
            init_directory=init_directory,
            scanner_type=scanner_type,
            note=note,
        )

        scanner_initalization_data.additional_properties = d
        return scanner_initalization_data

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
