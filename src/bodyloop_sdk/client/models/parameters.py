from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analyzed_avatar_3d_parameters import AnalyzedAvatar3DParameters
    from ..models.avatar_3d_parameters_output import Avatar3DParametersOutput
    from ..models.image_set_2d_parameters import ImageSet2DParameters
    from ..models.mesh_3d_parameters import Mesh3DParameters
    from ..models.meta import Meta
    from ..models.report_parameters import ReportParameters


T = TypeVar("T", bound="Parameters")


@_attrs_define
class Parameters:
    """Extended version of `ParametersData` that includes parameters_id and meta infomration"""

    parameters_id: int
    title: str | Unset = ""
    imageset_2d: ImageSet2DParameters | None | Unset = UNSET
    mesh_3d: Mesh3DParameters | None | Unset = UNSET
    avatar_3d: Avatar3DParametersOutput | None | Unset = UNSET
    analyzed_avatar_3d: AnalyzedAvatar3DParameters | None | Unset = UNSET
    report: None | ReportParameters | Unset = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analyzed_avatar_3d_parameters import AnalyzedAvatar3DParameters
        from ..models.avatar_3d_parameters_output import Avatar3DParametersOutput
        from ..models.image_set_2d_parameters import ImageSet2DParameters
        from ..models.mesh_3d_parameters import Mesh3DParameters
        from ..models.meta import Meta
        from ..models.report_parameters import ReportParameters

        parameters_id = self.parameters_id

        title = self.title

        imageset_2d: dict[str, Any] | None | Unset
        if isinstance(self.imageset_2d, Unset):
            imageset_2d = UNSET
        elif isinstance(self.imageset_2d, ImageSet2DParameters):
            imageset_2d = self.imageset_2d.to_dict()
        else:
            imageset_2d = self.imageset_2d

        mesh_3d: dict[str, Any] | None | Unset
        if isinstance(self.mesh_3d, Unset):
            mesh_3d = UNSET
        elif isinstance(self.mesh_3d, Mesh3DParameters):
            mesh_3d = self.mesh_3d.to_dict()
        else:
            mesh_3d = self.mesh_3d

        avatar_3d: dict[str, Any] | None | Unset
        if isinstance(self.avatar_3d, Unset):
            avatar_3d = UNSET
        elif isinstance(self.avatar_3d, Avatar3DParametersOutput):
            avatar_3d = self.avatar_3d.to_dict()
        else:
            avatar_3d = self.avatar_3d

        analyzed_avatar_3d: dict[str, Any] | None | Unset
        if isinstance(self.analyzed_avatar_3d, Unset):
            analyzed_avatar_3d = UNSET
        elif isinstance(self.analyzed_avatar_3d, AnalyzedAvatar3DParameters):
            analyzed_avatar_3d = self.analyzed_avatar_3d.to_dict()
        else:
            analyzed_avatar_3d = self.analyzed_avatar_3d

        report: dict[str, Any] | None | Unset
        if isinstance(self.report, Unset):
            report = UNSET
        elif isinstance(self.report, ReportParameters):
            report = self.report.to_dict()
        else:
            report = self.report

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
                "parameters_id": parameters_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if imageset_2d is not UNSET:
            field_dict["imageset_2d"] = imageset_2d
        if mesh_3d is not UNSET:
            field_dict["mesh_3d"] = mesh_3d
        if avatar_3d is not UNSET:
            field_dict["avatar_3d"] = avatar_3d
        if analyzed_avatar_3d is not UNSET:
            field_dict["analyzed_avatar_3d"] = analyzed_avatar_3d
        if report is not UNSET:
            field_dict["report"] = report
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analyzed_avatar_3d_parameters import AnalyzedAvatar3DParameters
        from ..models.avatar_3d_parameters_output import Avatar3DParametersOutput
        from ..models.image_set_2d_parameters import ImageSet2DParameters
        from ..models.mesh_3d_parameters import Mesh3DParameters
        from ..models.meta import Meta
        from ..models.report_parameters import ReportParameters

        d = dict(src_dict)
        parameters_id = d.pop("parameters_id")

        title = d.pop("title", UNSET)

        def _parse_imageset_2d(data: object) -> ImageSet2DParameters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                imageset_2d_type_0 = ImageSet2DParameters.from_dict(data)

                return imageset_2d_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageSet2DParameters | None | Unset, data)

        imageset_2d = _parse_imageset_2d(d.pop("imageset_2d", UNSET))

        def _parse_mesh_3d(data: object) -> Mesh3DParameters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mesh_3d_type_0 = Mesh3DParameters.from_dict(data)

                return mesh_3d_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Mesh3DParameters | None | Unset, data)

        mesh_3d = _parse_mesh_3d(d.pop("mesh_3d", UNSET))

        def _parse_avatar_3d(data: object) -> Avatar3DParametersOutput | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                avatar_3d_type_0 = Avatar3DParametersOutput.from_dict(data)

                return avatar_3d_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Avatar3DParametersOutput | None | Unset, data)

        avatar_3d = _parse_avatar_3d(d.pop("avatar_3d", UNSET))

        def _parse_analyzed_avatar_3d(data: object) -> AnalyzedAvatar3DParameters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                analyzed_avatar_3d_type_0 = AnalyzedAvatar3DParameters.from_dict(data)

                return analyzed_avatar_3d_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyzedAvatar3DParameters | None | Unset, data)

        analyzed_avatar_3d = _parse_analyzed_avatar_3d(d.pop("analyzed_avatar_3d", UNSET))

        def _parse_report(data: object) -> None | ReportParameters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_type_0 = ReportParameters.from_dict(data)

                return report_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportParameters | Unset, data)

        report = _parse_report(d.pop("report", UNSET))

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

        parameters = cls(
            parameters_id=parameters_id,
            title=title,
            imageset_2d=imageset_2d,
            mesh_3d=mesh_3d,
            avatar_3d=avatar_3d,
            analyzed_avatar_3d=analyzed_avatar_3d,
            report=report,
            meta=meta,
        )

        parameters.additional_properties = d
        return parameters

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
