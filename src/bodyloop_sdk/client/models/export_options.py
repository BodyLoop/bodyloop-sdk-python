from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_options_avatar_3d_format_type_0 import (
    ExportOptionsAvatar3DFormatType0,
    check_export_options_avatar_3d_format_type_0,
)
from ..models.export_options_measurements_format_type_0 import (
    ExportOptionsMeasurementsFormatType0,
    check_export_options_measurements_format_type_0,
)
from ..models.export_options_mesh_3d_format_type_0 import (
    ExportOptionsMesh3DFormatType0,
    check_export_options_mesh_3d_format_type_0,
)
from ..models.export_options_view_format_type_0 import (
    ExportOptionsViewFormatType0,
    check_export_options_view_format_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportOptions")


@_attrs_define
class ExportOptions:
    """Options for Viatar export"""

    measurements_format: ExportOptionsMeasurementsFormatType0 | None | Unset = UNSET
    contour_format: Literal["svg"] | None | Unset = UNSET
    mesh_3d_format: ExportOptionsMesh3DFormatType0 | None | Unset = UNSET
    avatar_3d_format: ExportOptionsAvatar3DFormatType0 | None | Unset = UNSET
    view_format: ExportOptionsViewFormatType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurements_format: None | str | Unset
        if isinstance(self.measurements_format, Unset):
            measurements_format = UNSET
        elif isinstance(self.measurements_format, str):
            measurements_format = self.measurements_format
        else:
            measurements_format = self.measurements_format

        contour_format: Literal["svg"] | None | Unset
        if isinstance(self.contour_format, Unset):
            contour_format = UNSET
        else:
            contour_format = self.contour_format

        mesh_3d_format: None | str | Unset
        if isinstance(self.mesh_3d_format, Unset):
            mesh_3d_format = UNSET
        elif isinstance(self.mesh_3d_format, str):
            mesh_3d_format = self.mesh_3d_format
        else:
            mesh_3d_format = self.mesh_3d_format

        avatar_3d_format: None | str | Unset
        if isinstance(self.avatar_3d_format, Unset):
            avatar_3d_format = UNSET
        elif isinstance(self.avatar_3d_format, str):
            avatar_3d_format = self.avatar_3d_format
        else:
            avatar_3d_format = self.avatar_3d_format

        view_format: None | str | Unset
        if isinstance(self.view_format, Unset):
            view_format = UNSET
        elif isinstance(self.view_format, str):
            view_format = self.view_format
        else:
            view_format = self.view_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurements_format is not UNSET:
            field_dict["measurements_format"] = measurements_format
        if contour_format is not UNSET:
            field_dict["contour_format"] = contour_format
        if mesh_3d_format is not UNSET:
            field_dict["mesh_3d_format"] = mesh_3d_format
        if avatar_3d_format is not UNSET:
            field_dict["avatar_3d_format"] = avatar_3d_format
        if view_format is not UNSET:
            field_dict["view_format"] = view_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_measurements_format(data: object) -> ExportOptionsMeasurementsFormatType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                measurements_format_type_0 = check_export_options_measurements_format_type_0(data)

                return measurements_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportOptionsMeasurementsFormatType0 | None | Unset, data)

        measurements_format = _parse_measurements_format(d.pop("measurements_format", UNSET))

        def _parse_contour_format(data: object) -> Literal["svg"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            contour_format_type_0 = cast(Literal["svg"], data)
            if contour_format_type_0 != "svg":
                raise ValueError(f"contour_format_type_0 must match const 'svg', got '{contour_format_type_0}'")
            return contour_format_type_0
            return cast(Literal["svg"] | None | Unset, data)

        contour_format = _parse_contour_format(d.pop("contour_format", UNSET))

        def _parse_mesh_3d_format(data: object) -> ExportOptionsMesh3DFormatType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mesh_3d_format_type_0 = check_export_options_mesh_3d_format_type_0(data)

                return mesh_3d_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportOptionsMesh3DFormatType0 | None | Unset, data)

        mesh_3d_format = _parse_mesh_3d_format(d.pop("mesh_3d_format", UNSET))

        def _parse_avatar_3d_format(data: object) -> ExportOptionsAvatar3DFormatType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                avatar_3d_format_type_0 = check_export_options_avatar_3d_format_type_0(data)

                return avatar_3d_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportOptionsAvatar3DFormatType0 | None | Unset, data)

        avatar_3d_format = _parse_avatar_3d_format(d.pop("avatar_3d_format", UNSET))

        def _parse_view_format(data: object) -> ExportOptionsViewFormatType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                view_format_type_0 = check_export_options_view_format_type_0(data)

                return view_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportOptionsViewFormatType0 | None | Unset, data)

        view_format = _parse_view_format(d.pop("view_format", UNSET))

        export_options = cls(
            measurements_format=measurements_format,
            contour_format=contour_format,
            mesh_3d_format=mesh_3d_format,
            avatar_3d_format=avatar_3d_format,
            view_format=view_format,
        )

        export_options.additional_properties = d
        return export_options

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
