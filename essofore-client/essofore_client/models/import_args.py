from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_type import DocumentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_args_metadata import ImportArgsMetadata


T = TypeVar("T", bound="ImportArgs")


@_attrs_define
class ImportArgs:
    """
    Attributes:
        title (str):
        source_url (str):
        doc_type (DocumentType):
        metadata (Union[Unset, ImportArgsMetadata]):
    """

    title: str
    source_url: str
    doc_type: DocumentType
    metadata: Union[Unset, "ImportArgsMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        source_url = self.source_url

        doc_type = self.doc_type.value

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "sourceUrl": source_url,
                "docType": doc_type,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.import_args_metadata import ImportArgsMetadata

        d = src_dict.copy()
        title = d.pop("title")

        source_url = d.pop("sourceUrl")

        doc_type = DocumentType(d.pop("docType"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ImportArgsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ImportArgsMetadata.from_dict(_metadata)

        import_args = cls(
            title=title,
            source_url=source_url,
            doc_type=doc_type,
            metadata=metadata,
        )

        import_args.additional_properties = d
        return import_args

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
