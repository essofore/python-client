"""Contains all the data models used in inputs/outputs"""

from .bad_request import BadRequest
from .catalog_entry import CatalogEntry
from .catalog_info import CatalogInfo
from .collection_info import CollectionInfo
from .create_collection_metadata import CreateCollectionMetadata
from .document_info import DocumentInfo
from .document_type import DocumentType
from .download_document_metadata import DownloadDocumentMetadata
from .import_args import ImportArgs
from .import_args_metadata import ImportArgsMetadata
from .metadata_mode import MetadataMode
from .search_result import SearchResult
from .unprocessable_content import UnprocessableContent
from .update_collection_metadata import UpdateCollectionMetadata
from .update_document_metadata import UpdateDocumentMetadata
from .upload_document_metadata import UploadDocumentMetadata
from .violation import Violation

__all__ = (
    "BadRequest",
    "CatalogEntry",
    "CatalogInfo",
    "CollectionInfo",
    "CreateCollectionMetadata",
    "DocumentInfo",
    "DocumentType",
    "DownloadDocumentMetadata",
    "ImportArgs",
    "ImportArgsMetadata",
    "MetadataMode",
    "SearchResult",
    "UnprocessableContent",
    "UpdateCollectionMetadata",
    "UpdateDocumentMetadata",
    "UploadDocumentMetadata",
    "Violation",
)
