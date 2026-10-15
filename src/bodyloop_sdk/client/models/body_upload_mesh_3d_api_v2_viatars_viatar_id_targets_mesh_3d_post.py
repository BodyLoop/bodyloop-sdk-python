from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost")


@_attrs_define
class BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost:
    mesh_3d: File
    control_points: File | None | Unset = UNSET
    registration: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mesh_3d = self.mesh_3d.to_tuple()

        control_points: FileTypes | None | Unset
        if isinstance(self.control_points, Unset):
            control_points = UNSET
        elif isinstance(self.control_points, File):
            control_points = self.control_points.to_tuple()

        else:
            control_points = self.control_points

        registration: FileTypes | None | Unset
        if isinstance(self.registration, Unset):
            registration = UNSET
        elif isinstance(self.registration, File):
            registration = self.registration.to_tuple()

        else:
            registration = self.registration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mesh_3d": mesh_3d,
            }
        )
        if control_points is not UNSET:
            field_dict["control_points"] = control_points
        if registration is not UNSET:
            field_dict["registration"] = registration

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("mesh_3d", self.mesh_3d.to_tuple()))

        if not isinstance(self.control_points, Unset):
            if isinstance(self.control_points, File):
                files.append(("control_points", self.control_points.to_tuple()))
            else:
                files.append(("control_points", (None, str(self.control_points).encode(), "text/plain")))

        if not isinstance(self.registration, Unset):
            if isinstance(self.registration, File):
                files.append(("registration", self.registration.to_tuple()))
            else:
                files.append(("registration", (None, str(self.registration).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mesh_3d = File(payload=BytesIO(d.pop("mesh_3d")))

        def _parse_control_points(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                control_points_type_0 = File(payload=BytesIO(data))

                return control_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        control_points = _parse_control_points(d.pop("control_points", UNSET))

        def _parse_registration(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                registration_type_0 = File(payload=BytesIO(data))

                return registration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        registration = _parse_registration(d.pop("registration", UNSET))

        body_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post = cls(
            mesh_3d=mesh_3d,
            control_points=control_points,
            registration=registration,
        )

        body_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post.additional_properties = d
        return body_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post

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
