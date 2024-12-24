from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocumentInfo")


@_attrs_define
class DocumentInfo:
    """
    Attributes:
        collection_id (str):
        document_id (str):
        title (str):
        sample_text (str):
        embeddings_count (int):
        size (int):
    """

    collection_id: str
    document_id: str
    title: str
    sample_text: str
    embeddings_count: int
    size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_id = self.collection_id

        document_id = self.document_id

        title = self.title

        sample_text = self.sample_text

        embeddings_count = self.embeddings_count

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionId": collection_id,
                "documentId": document_id,
                "title": title,
                "sampleText": sample_text,
                "embeddingsCount": embeddings_count,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_id = d.pop("collectionId")

        document_id = d.pop("documentId")

        title = d.pop("title")

        sample_text = d.pop("sampleText")

        embeddings_count = d.pop("embeddingsCount")

        size = d.pop("size")

        document_info = cls(
            collection_id=collection_id,
            document_id=document_id,
            title=title,
            sample_text=sample_text,
            embeddings_count=embeddings_count,
            size=size,
        )

        document_info.additional_properties = d
        return document_info

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
