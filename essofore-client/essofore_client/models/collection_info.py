from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document_info import DocumentInfo


T = TypeVar("T", bound="CollectionInfo")


@_attrs_define
class CollectionInfo:
    """
    Attributes:
        id (str):
        size (int):
        title (str):
        documents (List['DocumentInfo']):
    """

    id: str
    size: int
    title: str
    documents: List["DocumentInfo"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        size = self.size

        title = self.title

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "size": size,
                "title": title,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_info import DocumentInfo

        d = src_dict.copy()
        id = d.pop("id")

        size = d.pop("size")

        title = d.pop("title")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = DocumentInfo.from_dict(documents_item_data)

            documents.append(documents_item)

        collection_info = cls(
            id=id,
            size=size,
            title=title,
            documents=documents,
        )

        collection_info.additional_properties = d
        return collection_info

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
