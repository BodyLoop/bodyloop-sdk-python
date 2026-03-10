from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_dataprocessor_type_0 import ModelsDataprocessorType0
    from ..models.models_photogrammetry_type_0 import ModelsPhotogrammetryType0


T = TypeVar("T", bound="Models")


@_attrs_define
class Models:
    """Represents models of various categorys"""

    photogrammetry: ModelsPhotogrammetryType0 | None | Unset = UNSET
    dataprocessor: ModelsDataprocessorType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.models_dataprocessor_type_0 import ModelsDataprocessorType0
        from ..models.models_photogrammetry_type_0 import ModelsPhotogrammetryType0

        photogrammetry: dict[str, Any] | None | Unset
        if isinstance(self.photogrammetry, Unset):
            photogrammetry = UNSET
        elif isinstance(self.photogrammetry, ModelsPhotogrammetryType0):
            photogrammetry = self.photogrammetry.to_dict()
        else:
            photogrammetry = self.photogrammetry

        dataprocessor: dict[str, Any] | None | Unset
        if isinstance(self.dataprocessor, Unset):
            dataprocessor = UNSET
        elif isinstance(self.dataprocessor, ModelsDataprocessorType0):
            dataprocessor = self.dataprocessor.to_dict()
        else:
            dataprocessor = self.dataprocessor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if photogrammetry is not UNSET:
            field_dict["photogrammetry"] = photogrammetry
        if dataprocessor is not UNSET:
            field_dict["dataprocessor"] = dataprocessor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_dataprocessor_type_0 import ModelsDataprocessorType0
        from ..models.models_photogrammetry_type_0 import ModelsPhotogrammetryType0

        d = dict(src_dict)

        def _parse_photogrammetry(data: object) -> ModelsPhotogrammetryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                photogrammetry_type_0 = ModelsPhotogrammetryType0.from_dict(data)

                return photogrammetry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsPhotogrammetryType0 | None | Unset, data)

        photogrammetry = _parse_photogrammetry(d.pop("photogrammetry", UNSET))

        def _parse_dataprocessor(data: object) -> ModelsDataprocessorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dataprocessor_type_0 = ModelsDataprocessorType0.from_dict(data)

                return dataprocessor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsDataprocessorType0 | None | Unset, data)

        dataprocessor = _parse_dataprocessor(d.pop("dataprocessor", UNSET))

        models = cls(
            photogrammetry=photogrammetry,
            dataprocessor=dataprocessor,
        )

        models.additional_properties = d
        return models

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
