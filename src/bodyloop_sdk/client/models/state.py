from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_acquisition_state import StateAcquisitionState
    from ..models.state_backend_state import StateBackendState
    from ..models.state_general_state import StateGeneralState
    from ..models.state_initialization_state import StateInitializationState


T = TypeVar("T", bound="State")


@_attrs_define
class State:
    """Representation of a State"""

    general_state: StateGeneralState | Unset = UNSET
    backend_state: StateBackendState | Unset = UNSET
    initialization_state: StateInitializationState | Unset = UNSET
    acquisition_state: StateAcquisitionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        general_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.general_state, Unset):
            general_state = self.general_state.to_dict()

        backend_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backend_state, Unset):
            backend_state = self.backend_state.to_dict()

        initialization_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.initialization_state, Unset):
            initialization_state = self.initialization_state.to_dict()

        acquisition_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acquisition_state, Unset):
            acquisition_state = self.acquisition_state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if general_state is not UNSET:
            field_dict["General_State"] = general_state
        if backend_state is not UNSET:
            field_dict["Backend_State"] = backend_state
        if initialization_state is not UNSET:
            field_dict["Initialization_State"] = initialization_state
        if acquisition_state is not UNSET:
            field_dict["Acquisition_State"] = acquisition_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_acquisition_state import StateAcquisitionState
        from ..models.state_backend_state import StateBackendState
        from ..models.state_general_state import StateGeneralState
        from ..models.state_initialization_state import StateInitializationState

        d = dict(src_dict)
        _general_state = d.pop("General_State", UNSET)
        general_state: StateGeneralState | Unset
        if isinstance(_general_state, Unset):
            general_state = UNSET
        else:
            general_state = StateGeneralState.from_dict(_general_state)

        _backend_state = d.pop("Backend_State", UNSET)
        backend_state: StateBackendState | Unset
        if isinstance(_backend_state, Unset):
            backend_state = UNSET
        else:
            backend_state = StateBackendState.from_dict(_backend_state)

        _initialization_state = d.pop("Initialization_State", UNSET)
        initialization_state: StateInitializationState | Unset
        if isinstance(_initialization_state, Unset):
            initialization_state = UNSET
        else:
            initialization_state = StateInitializationState.from_dict(_initialization_state)

        _acquisition_state = d.pop("Acquisition_State", UNSET)
        acquisition_state: StateAcquisitionState | Unset
        if isinstance(_acquisition_state, Unset):
            acquisition_state = UNSET
        else:
            acquisition_state = StateAcquisitionState.from_dict(_acquisition_state)

        state = cls(
            general_state=general_state,
            backend_state=backend_state,
            initialization_state=initialization_state,
            acquisition_state=acquisition_state,
        )

        state.additional_properties = d
        return state

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
