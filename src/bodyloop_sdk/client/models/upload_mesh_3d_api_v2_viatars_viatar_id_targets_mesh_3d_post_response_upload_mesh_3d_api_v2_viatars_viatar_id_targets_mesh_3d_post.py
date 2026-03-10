from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.biomech_system_manager_models_viatar_target import BiomechSystemManagerModelsViatarTarget


T = TypeVar(
    "T",
    bound="UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost",
)


@_attrs_define
class UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost:
    additional_properties: dict[str, BiomechSystemManagerModelsViatarTarget] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.biomech_system_manager_models_viatar_target import BiomechSystemManagerModelsViatarTarget

        d = dict(src_dict)
        upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post_response_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BiomechSystemManagerModelsViatarTarget.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post_response_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post.additional_properties = additional_properties
        return upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post_response_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BiomechSystemManagerModelsViatarTarget:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BiomechSystemManagerModelsViatarTarget) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
