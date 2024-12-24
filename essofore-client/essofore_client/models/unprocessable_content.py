from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnprocessableContent")


@_attrs_define
class UnprocessableContent:
    """
    Attributes:
        timestamp (Union[Unset, str]):
        status (Union[Unset, str]):
        path (Union[Unset, str]):
        message (Union[Unset, str]):
        error (Union[Unset, str]):
    """

    timestamp: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp

        status = self.status

        path = self.path

        message = self.message

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if path is not UNSET:
            field_dict["path"] = path
        if message is not UNSET:
            field_dict["message"] = message
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp", UNSET)

        status = d.pop("status", UNSET)

        path = d.pop("path", UNSET)

        message = d.pop("message", UNSET)

        error = d.pop("error", UNSET)

        unprocessable_content = cls(
            timestamp=timestamp,
            status=status,
            path=path,
            message=message,
            error=error,
        )

        unprocessable_content.additional_properties = d
        return unprocessable_content

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
