from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogEntry")


@_attrs_define
class CatalogEntry:
    """
    Attributes:
        collection_id (str):
        collection_title (str):
        document_count (int):
        embeddings_count (int):
        size (int):
    """

    collection_id: str
    collection_title: str
    document_count: int
    embeddings_count: int
    size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_id = self.collection_id

        collection_title = self.collection_title

        document_count = self.document_count

        embeddings_count = self.embeddings_count

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionId": collection_id,
                "collectionTitle": collection_title,
                "documentCount": document_count,
                "embeddingsCount": embeddings_count,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_id = d.pop("collectionId")

        collection_title = d.pop("collectionTitle")

        document_count = d.pop("documentCount")

        embeddings_count = d.pop("embeddingsCount")

        size = d.pop("size")

        catalog_entry = cls(
            collection_id=collection_id,
            collection_title=collection_title,
            document_count=document_count,
            embeddings_count=embeddings_count,
            size=size,
        )

        catalog_entry.additional_properties = d
        return catalog_entry

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
