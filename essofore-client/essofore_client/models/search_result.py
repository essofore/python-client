from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        document_id (str):
        title (str):
        text (str):
        distance (float):
        order (int):
    """

    document_id: str
    title: str
    text: str
    distance: float
    order: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id

        title = self.title

        text = self.text

        distance = self.distance

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "title": title,
                "text": text,
                "distance": distance,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        title = d.pop("title")

        text = d.pop("text")

        distance = d.pop("distance")

        order = d.pop("order")

        search_result = cls(
            document_id=document_id,
            title=title,
            text=text,
            distance=distance,
            order=order,
        )

        search_result.additional_properties = d
        return search_result

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
