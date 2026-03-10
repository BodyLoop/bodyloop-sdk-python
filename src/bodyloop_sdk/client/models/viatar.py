from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images import Images
    from ..models.meta import Meta
    from ..models.models import Models
    from ..models.parameters_data_output import ParametersDataOutput
    from ..models.viatar_angles_type_0 import ViatarAnglesType0
    from ..models.viatar_axes_type_0 import ViatarAxesType0
    from ..models.viatar_crosssections_type_0 import ViatarCrosssectionsType0
    from ..models.viatar_data_series import ViatarDataSeries
    from ..models.viatar_distances_type_0 import ViatarDistancesType0
    from ..models.viatar_heights_type_0 import ViatarHeightsType0
    from ..models.viatar_markers_type_0 import ViatarMarkersType0
    from ..models.viatar_observations_type_0 import ViatarObservationsType0
    from ..models.viatar_properties_type_0 import ViatarPropertiesType0
    from ..models.viatar_targets_type_0 import ViatarTargetsType0


T = TypeVar("T", bound="Viatar")


@_attrs_define
class Viatar:
    """Extended version of `ViatarData` that includes unique viatar_id and meta information.

    Example:
        {'note': 'A default viatar.', 'observations': {}, 'parameters': {'analyzed_avatar_3d':
            {'orphaned_palpation_marker': True, 'palp_snap_distance': 0.05, 'preset_id': -1}, 'avatar_3d': {'clothing':
            'Tight', 'model': 'No Model', 'reverse': False}, 'imageset_2d': {'exposure_time': 30000, 'keep_images': False,
            'mass_from_phd': False, 'projector_brightness': 83, 'ring_brightness': 40}, 'mesh_3d': {'detail': 'High',
            'texture': True}, 'report': {'preset': 'Default'}, 'title': ''}}

    """

    viatar_id: int
    proband_id: int | None | Unset = UNSET
    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    parameters: None | ParametersDataOutput | Unset = UNSET
    targets: None | Unset | ViatarTargetsType0 = UNSET
    observations: None | Unset | ViatarObservationsType0 = UNSET
    scan_folder: None | str | Unset = UNSET
    images: Images | None | Unset = UNSET
    models: Models | None | Unset = UNSET
    applied_presets: list[int] | None | Unset = UNSET
    properties: None | Unset | ViatarPropertiesType0 = UNSET
    markers: None | Unset | ViatarMarkersType0 = UNSET
    heights: None | Unset | ViatarHeightsType0 = UNSET
    distances: None | Unset | ViatarDistancesType0 = UNSET
    crosssections: None | Unset | ViatarCrosssectionsType0 = UNSET
    angles: None | Unset | ViatarAnglesType0 = UNSET
    axes: None | Unset | ViatarAxesType0 = UNSET
    series: None | Unset | ViatarDataSeries = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.images import Images
        from ..models.meta import Meta
        from ..models.models import Models
        from ..models.parameters_data_output import ParametersDataOutput
        from ..models.viatar_angles_type_0 import ViatarAnglesType0
        from ..models.viatar_axes_type_0 import ViatarAxesType0
        from ..models.viatar_crosssections_type_0 import ViatarCrosssectionsType0
        from ..models.viatar_data_series import ViatarDataSeries
        from ..models.viatar_distances_type_0 import ViatarDistancesType0
        from ..models.viatar_heights_type_0 import ViatarHeightsType0
        from ..models.viatar_markers_type_0 import ViatarMarkersType0
        from ..models.viatar_observations_type_0 import ViatarObservationsType0
        from ..models.viatar_properties_type_0 import ViatarPropertiesType0
        from ..models.viatar_targets_type_0 import ViatarTargetsType0

        viatar_id = self.viatar_id

        proband_id: int | None | Unset
        if isinstance(self.proband_id, Unset):
            proband_id = UNSET
        else:
            proband_id = self.proband_id

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

        parameters: dict[str, Any] | None | Unset
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, ParametersDataOutput):
            parameters = self.parameters.to_dict()
        else:
            parameters = self.parameters

        targets: dict[str, Any] | None | Unset
        if isinstance(self.targets, Unset):
            targets = UNSET
        elif isinstance(self.targets, ViatarTargetsType0):
            targets = self.targets.to_dict()
        else:
            targets = self.targets

        observations: dict[str, Any] | None | Unset
        if isinstance(self.observations, Unset):
            observations = UNSET
        elif isinstance(self.observations, ViatarObservationsType0):
            observations = self.observations.to_dict()
        else:
            observations = self.observations

        scan_folder: None | str | Unset
        if isinstance(self.scan_folder, Unset):
            scan_folder = UNSET
        else:
            scan_folder = self.scan_folder

        images: dict[str, Any] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, Images):
            images = self.images.to_dict()
        else:
            images = self.images

        models: dict[str, Any] | None | Unset
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, Models):
            models = self.models.to_dict()
        else:
            models = self.models

        applied_presets: list[int] | None | Unset
        if isinstance(self.applied_presets, Unset):
            applied_presets = UNSET
        elif isinstance(self.applied_presets, list):
            applied_presets = self.applied_presets

        else:
            applied_presets = self.applied_presets

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, ViatarPropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        markers: dict[str, Any] | None | Unset
        if isinstance(self.markers, Unset):
            markers = UNSET
        elif isinstance(self.markers, ViatarMarkersType0):
            markers = self.markers.to_dict()
        else:
            markers = self.markers

        heights: dict[str, Any] | None | Unset
        if isinstance(self.heights, Unset):
            heights = UNSET
        elif isinstance(self.heights, ViatarHeightsType0):
            heights = self.heights.to_dict()
        else:
            heights = self.heights

        distances: dict[str, Any] | None | Unset
        if isinstance(self.distances, Unset):
            distances = UNSET
        elif isinstance(self.distances, ViatarDistancesType0):
            distances = self.distances.to_dict()
        else:
            distances = self.distances

        crosssections: dict[str, Any] | None | Unset
        if isinstance(self.crosssections, Unset):
            crosssections = UNSET
        elif isinstance(self.crosssections, ViatarCrosssectionsType0):
            crosssections = self.crosssections.to_dict()
        else:
            crosssections = self.crosssections

        angles: dict[str, Any] | None | Unset
        if isinstance(self.angles, Unset):
            angles = UNSET
        elif isinstance(self.angles, ViatarAnglesType0):
            angles = self.angles.to_dict()
        else:
            angles = self.angles

        axes: dict[str, Any] | None | Unset
        if isinstance(self.axes, Unset):
            axes = UNSET
        elif isinstance(self.axes, ViatarAxesType0):
            axes = self.axes.to_dict()
        else:
            axes = self.axes

        series: dict[str, Any] | None | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        elif isinstance(self.series, ViatarDataSeries):
            series = self.series.to_dict()
        else:
            series = self.series

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
                "viatar_id": viatar_id,
            }
        )
        if proband_id is not UNSET:
            field_dict["proband_id"] = proband_id
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if targets is not UNSET:
            field_dict["targets"] = targets
        if observations is not UNSET:
            field_dict["observations"] = observations
        if scan_folder is not UNSET:
            field_dict["scan_folder"] = scan_folder
        if images is not UNSET:
            field_dict["images"] = images
        if models is not UNSET:
            field_dict["models"] = models
        if applied_presets is not UNSET:
            field_dict["applied_presets"] = applied_presets
        if properties is not UNSET:
            field_dict["properties"] = properties
        if markers is not UNSET:
            field_dict["markers"] = markers
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
        if series is not UNSET:
            field_dict["series"] = series
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images import Images
        from ..models.meta import Meta
        from ..models.models import Models
        from ..models.parameters_data_output import ParametersDataOutput
        from ..models.viatar_angles_type_0 import ViatarAnglesType0
        from ..models.viatar_axes_type_0 import ViatarAxesType0
        from ..models.viatar_crosssections_type_0 import ViatarCrosssectionsType0
        from ..models.viatar_data_series import ViatarDataSeries
        from ..models.viatar_distances_type_0 import ViatarDistancesType0
        from ..models.viatar_heights_type_0 import ViatarHeightsType0
        from ..models.viatar_markers_type_0 import ViatarMarkersType0
        from ..models.viatar_observations_type_0 import ViatarObservationsType0
        from ..models.viatar_properties_type_0 import ViatarPropertiesType0
        from ..models.viatar_targets_type_0 import ViatarTargetsType0

        d = dict(src_dict)
        viatar_id = d.pop("viatar_id")

        def _parse_proband_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proband_id = _parse_proband_id(d.pop("proband_id", UNSET))

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

        def _parse_parameters(data: object) -> None | ParametersDataOutput | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0 = ParametersDataOutput.from_dict(data)

                return parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ParametersDataOutput | Unset, data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        def _parse_targets(data: object) -> None | Unset | ViatarTargetsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                targets_type_0 = ViatarTargetsType0.from_dict(data)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarTargetsType0, data)

        targets = _parse_targets(d.pop("targets", UNSET))

        def _parse_observations(data: object) -> None | Unset | ViatarObservationsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                observations_type_0 = ViatarObservationsType0.from_dict(data)

                return observations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarObservationsType0, data)

        observations = _parse_observations(d.pop("observations", UNSET))

        def _parse_scan_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_folder = _parse_scan_folder(d.pop("scan_folder", UNSET))

        def _parse_images(data: object) -> Images | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0 = Images.from_dict(data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Images | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_models(data: object) -> Models | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                models_type_0 = Models.from_dict(data)

                return models_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Models | None | Unset, data)

        models = _parse_models(d.pop("models", UNSET))

        def _parse_applied_presets(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applied_presets_type_0 = cast(list[int], data)

                return applied_presets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        applied_presets = _parse_applied_presets(d.pop("applied_presets", UNSET))

        def _parse_properties(data: object) -> None | Unset | ViatarPropertiesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = ViatarPropertiesType0.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarPropertiesType0, data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_markers(data: object) -> None | Unset | ViatarMarkersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                markers_type_0 = ViatarMarkersType0.from_dict(data)

                return markers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarMarkersType0, data)

        markers = _parse_markers(d.pop("markers", UNSET))

        def _parse_heights(data: object) -> None | Unset | ViatarHeightsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                heights_type_0 = ViatarHeightsType0.from_dict(data)

                return heights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarHeightsType0, data)

        heights = _parse_heights(d.pop("heights", UNSET))

        def _parse_distances(data: object) -> None | Unset | ViatarDistancesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distances_type_0 = ViatarDistancesType0.from_dict(data)

                return distances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarDistancesType0, data)

        distances = _parse_distances(d.pop("distances", UNSET))

        def _parse_crosssections(data: object) -> None | Unset | ViatarCrosssectionsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crosssections_type_0 = ViatarCrosssectionsType0.from_dict(data)

                return crosssections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarCrosssectionsType0, data)

        crosssections = _parse_crosssections(d.pop("crosssections", UNSET))

        def _parse_angles(data: object) -> None | Unset | ViatarAnglesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                angles_type_0 = ViatarAnglesType0.from_dict(data)

                return angles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarAnglesType0, data)

        angles = _parse_angles(d.pop("angles", UNSET))

        def _parse_axes(data: object) -> None | Unset | ViatarAxesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                axes_type_0 = ViatarAxesType0.from_dict(data)

                return axes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarAxesType0, data)

        axes = _parse_axes(d.pop("axes", UNSET))

        def _parse_series(data: object) -> None | Unset | ViatarDataSeries:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_type_0 = ViatarDataSeries.from_dict(data)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarDataSeries, data)

        series = _parse_series(d.pop("series", UNSET))

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

        viatar = cls(
            viatar_id=viatar_id,
            proband_id=proband_id,
            note=note,
            key_external=key_external,
            parameters=parameters,
            targets=targets,
            observations=observations,
            scan_folder=scan_folder,
            images=images,
            models=models,
            applied_presets=applied_presets,
            properties=properties,
            markers=markers,
            heights=heights,
            distances=distances,
            crosssections=crosssections,
            angles=angles,
            axes=axes,
            series=series,
            meta=meta,
        )

        viatar.additional_properties = d
        return viatar

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
