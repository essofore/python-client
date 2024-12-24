from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.documents import download_document
from essofore_client.models.document_type import DocumentType
from essofore_client.models import DocumentInfo
from essofore_client.models.download_document_metadata import DownloadDocumentMetadata
import shlex

# exit_on_error is broken. see: https://github.com/python/cpython/issues/85427
parser = argparse2.ArgumentParser(prog="download_document", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('--document_id', required=True)
parser.add_argument('--title', nargs='+', required=True)
parser.add_argument('--source_url', required=True)
parser.add_argument('--doc_type', required=True, choices=['txt', 'pdf', 'html', 'doc', 'xls', 'ppt', 'TXT','PDF','HTML','DOC','XLS','PPT'])
parser.add_argument('--metadata', nargs='+', action=argparse2.ParseKeyValuePairs, help='metadata expressed as key=value pairs', required=False, default={})

def exec(client, collection_id, document_id, title, source_url, doc_type, metadata):
    if metadata is not None:
        metadata = DownloadDocumentMetadata.from_dict(metadata)
    response = download_document.sync_detailed(client=client,
                                                collection_id = collection_id,
                                                document_id = document_id,
                                                title=title,
                                                source_url=source_url,
                                                doc_type=doc_type)
    if response.status_code == HTTPStatus.OK:
        doc_info : DocumentInfo = response.parsed
        embeddings_count = common.format_int(doc_info.embeddings_count)
        size = common.format_int(doc_info.size)
        print(f"created document with {embeddings_count} embeddings and size = {size} bytes")
    else:
        common.handle_http_error(response)

def validate(line):
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    if not args.collection_id:
        raise ValueError('collection_id cannot be null or blank')
    if not args.document_id:
        raise ValueError('document_id cannot be null or blank')    
    if not args.title or len(args.title) == 0:
        raise ValueError('title cannot be empty')
    args.title = ' '.join(args.title)
    if not args.title:
        raise ValueError('title cannot be empty')
    if not args.source_url:
        raise ValueError('source_url cannot be empty')
    if not args.doc_type:
        raise ValueError('doc_type cannot be empty')
    args.doc_type = DocumentType(args.doc_type.upper()) # will raise ValueError if it cannot convert string to enum
    return args

def execute(client, line):
    if client is None:
        raise ValueError('client is null')
    args = validate(line)
    return exec(client, args.collection_id, args.document_id, args.title, args.source_url, args.doc_type, args.metadata)
    