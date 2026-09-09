from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameters_data import ParametersData
    from ..models.viatar_data_attributes_external_type_0 import ViatarDataAttributesExternalType0
    from ..models.viatar_data_observations_type_0 import ViatarDataObservationsType0
    from ..models.viatar_data_targets_type_0 import ViatarDataTargetsType0


T = TypeVar("T", bound="ViatarData")


@_attrs_define
class ViatarData:
    """
    Example:
        {'note': 'A default viatar.', 'observations': {}, 'parameters': {'analyzed_avatar_3d':
            {'orphaned_palpation_marker': True, 'palp_snap_distance': 0.05, 'preset_id': -1}, 'avatar_3d': {'clothing':
            'Tight', 'model': 'No Model', 'reverse': False}, 'imageset_2d': {'exposure_time': 30000, 'keep_images': False,
            'projector_brightness': 83, 'ring_brightness': 40}, 'mesh_3d': {'detail': 'High', 'texture': True},
            'observations': {'weight': {}}, 'report': {'preset': 'Default'}, 'title': ''}}

    """

    proband_id: int | None | Unset = UNSET
    note: None | str | Unset = UNSET
    key_external: None | str | Unset = UNSET
    attributes_external: None | Unset | ViatarDataAttributesExternalType0 = UNSET
    parameters: ParametersData | Unset = UNSET
    """ Parameters influencing the target creation """
    observations: None | Unset | ViatarDataObservationsType0 = UNSET
    targets: None | Unset | ViatarDataTargetsType0 = UNSET
    scan_folder: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.viatar_data_attributes_external_type_0 import ViatarDataAttributesExternalType0  # noqa: PLC0415
        from ..models.viatar_data_observations_type_0 import ViatarDataObservationsType0  # noqa: PLC0415
        from ..models.viatar_data_targets_type_0 import ViatarDataTargetsType0  # noqa: PLC0415

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

        attributes_external: dict[str, Any] | None | Unset
        if isinstance(self.attributes_external, Unset):
            attributes_external = UNSET
        elif isinstance(self.attributes_external, ViatarDataAttributesExternalType0):
            attributes_external = self.attributes_external.to_dict()
        else:
            attributes_external = self.attributes_external

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        observations: dict[str, Any] | None | Unset
        if isinstance(self.observations, Unset):
            observations = UNSET
        elif isinstance(self.observations, ViatarDataObservationsType0):
            observations = self.observations.to_dict()
        else:
            observations = self.observations

        targets: dict[str, Any] | None | Unset
        if isinstance(self.targets, Unset):
            targets = UNSET
        elif isinstance(self.targets, ViatarDataTargetsType0):
            targets = self.targets.to_dict()
        else:
            targets = self.targets

        scan_folder: None | str | Unset
        if isinstance(self.scan_folder, Unset):
            scan_folder = UNSET
        else:
            scan_folder = self.scan_folder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proband_id is not UNSET:
            field_dict["proband_id"] = proband_id
        if note is not UNSET:
            field_dict["note"] = note
        if key_external is not UNSET:
            field_dict["key_external"] = key_external
        if attributes_external is not UNSET:
            field_dict["attributes_external"] = attributes_external
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if observations is not UNSET:
            field_dict["observations"] = observations
        if targets is not UNSET:
            field_dict["targets"] = targets
        if scan_folder is not UNSET:
            field_dict["scan_folder"] = scan_folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameters_data import ParametersData  # noqa: PLC0415
        from ..models.viatar_data_attributes_external_type_0 import ViatarDataAttributesExternalType0  # noqa: PLC0415
        from ..models.viatar_data_observations_type_0 import ViatarDataObservationsType0  # noqa: PLC0415
        from ..models.viatar_data_targets_type_0 import ViatarDataTargetsType0  # noqa: PLC0415

        d = dict(src_dict)

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

        def _parse_attributes_external(data: object) -> None | Unset | ViatarDataAttributesExternalType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_external_type_0 = ViatarDataAttributesExternalType0.from_dict(data)

                return attributes_external_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarDataAttributesExternalType0, data)

        attributes_external = _parse_attributes_external(d.pop("attributes_external", UNSET))

        _parameters = d.pop("parameters", UNSET)
        parameters: ParametersData | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ParametersData.from_dict(_parameters)

        def _parse_observations(data: object) -> None | Unset | ViatarDataObservationsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                observations_type_0 = ViatarDataObservationsType0.from_dict(data)

                return observations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarDataObservationsType0, data)

        observations = _parse_observations(d.pop("observations", UNSET))

        def _parse_targets(data: object) -> None | Unset | ViatarDataTargetsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                targets_type_0 = ViatarDataTargetsType0.from_dict(data)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViatarDataTargetsType0, data)

        targets = _parse_targets(d.pop("targets", UNSET))

        def _parse_scan_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_folder = _parse_scan_folder(d.pop("scan_folder", UNSET))

        viatar_data = cls(
            proband_id=proband_id,
            note=note,
            key_external=key_external,
            attributes_external=attributes_external,
            parameters=parameters,
            observations=observations,
            targets=targets,
            scan_folder=scan_folder,
        )

        viatar_data.additional_properties = d
        return viatar_data

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
