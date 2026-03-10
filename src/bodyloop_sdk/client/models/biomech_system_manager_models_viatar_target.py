from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.biomech_system_manager_models_viatar_target_state import BiomechSystemManagerModelsViatarTargetState
    from ..models.meta import Meta


T = TypeVar("T", bound="BiomechSystemManagerModelsViatarTarget")


@_attrs_define
class BiomechSystemManagerModelsViatarTarget:
    """Represents a target"""

    state: BiomechSystemManagerModelsViatarTargetState | Unset = UNSET
    """ Represents the state of a Target """
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, Meta):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.biomech_system_manager_models_viatar_target_state import (
            BiomechSystemManagerModelsViatarTargetState,
        )
        from ..models.meta import Meta

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: BiomechSystemManagerModelsViatarTargetState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BiomechSystemManagerModelsViatarTargetState.from_dict(_state)

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

        biomech_system_manager_models_viatar_target = cls(
            state=state,
            meta=meta,
        )

        biomech_system_manager_models_viatar_target.additional_properties = d
        return biomech_system_manager_models_viatar_target

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
