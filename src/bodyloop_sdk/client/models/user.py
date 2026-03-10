from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_user_group import UserUserGroup, check_user_user_group
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta import Meta
    from ..models.user_api_token import UserApiToken


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """User"""

    username: str
    full_name: str | Unset = UNSET
    user_group: UserUserGroup | Unset = UNSET
    disabled: bool | Unset = False
    api_token: UserApiToken | Unset = UNSET
    meta: Meta | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta

        username = self.username

        full_name = self.full_name

        user_group: str | Unset = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group

        disabled = self.disabled

        api_token: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_token, Unset):
            api_token = self.api_token.to_dict()

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
                "username": username,
            }
        )
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if user_group is not UNSET:
            field_dict["user_group"] = user_group
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if api_token is not UNSET:
            field_dict["api_token"] = api_token
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta import Meta
        from ..models.user_api_token import UserApiToken

        d = dict(src_dict)
        username = d.pop("username")

        full_name = d.pop("full_name", UNSET)

        _user_group = d.pop("user_group", UNSET)
        user_group: UserUserGroup | Unset
        if isinstance(_user_group, Unset):
            user_group = UNSET
        else:
            user_group = check_user_user_group(_user_group)

        disabled = d.pop("disabled", UNSET)

        _api_token = d.pop("api_token", UNSET)
        api_token: UserApiToken | Unset
        if isinstance(_api_token, Unset):
            api_token = UNSET
        else:
            api_token = UserApiToken.from_dict(_api_token)

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

        user = cls(
            username=username,
            full_name=full_name,
            user_group=user_group,
            disabled=disabled,
            api_token=api_token,
            meta=meta,
        )

        user.additional_properties = d
        return user

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
