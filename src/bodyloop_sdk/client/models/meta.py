from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """Meta information used by various classes"""

    crtime: datetime.datetime | None | Unset = UNSET
    mtime: datetime.datetime | None | Unset = UNSET
    info: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crtime: None | str | Unset
        if isinstance(self.crtime, Unset):
            crtime = UNSET
        elif isinstance(self.crtime, datetime.datetime):
            crtime = self.crtime.isoformat()
        else:
            crtime = self.crtime

        mtime: None | str | Unset
        if isinstance(self.mtime, Unset):
            mtime = UNSET
        elif isinstance(self.mtime, datetime.datetime):
            mtime = self.mtime.isoformat()
        else:
            mtime = self.mtime

        info: None | str | Unset
        if isinstance(self.info, Unset):
            info = UNSET
        else:
            info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crtime is not UNSET:
            field_dict["crtime"] = crtime
        if mtime is not UNSET:
            field_dict["mtime"] = mtime
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_crtime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crtime_type_0 = isoparse(data)

                return crtime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        crtime = _parse_crtime(d.pop("crtime", UNSET))

        def _parse_mtime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mtime_type_0 = isoparse(data)

                return mtime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        mtime = _parse_mtime(d.pop("mtime", UNSET))

        def _parse_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        info = _parse_info(d.pop("info", UNSET))

        meta = cls(
            crtime=crtime,
            mtime=mtime,
            info=info,
        )

        meta.additional_properties = d
        return meta

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
