from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.documents import update_document
from essofore_client.models.update_document_metadata import UpdateDocumentMetadata
from essofore_client.models.metadata_mode import MetadataMode
import shlex

# exit_on_error is broken. see: https://github.com/python/cpython/issues/85427
parser = argparse2.ArgumentParser(prog="update_document", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('--document_id', required=True)
parser.add_argument('--title', nargs='+', required=False)
parser.add_argument('--source_url', required=False)
parser.add_argument('--metadata', nargs='+', action=argparse2.ParseKeyValuePairs, help='metadata expressed as key=value pairs', required=False, default={})
parser.add_argument('--mode', required=False, choices=['update', 'replace'], default='update')

def exec(client, collection_id, document_id, title, source_url, metadata, mode):
    if metadata is not None:
        metadata = UpdateDocumentMetadata.from_dict(metadata)
    # ex: PUT http://localhost:8080/collections/1?author=Arthur%20Conan%20Doyle&publisher=Bantam%20Books
    response = update_document.sync_detailed(collection_id=collection_id, document_id=document_id, title=title, source_url=source_url, metadata=metadata, merge=MetadataMode(mode.upper()), client=client)
    if response.status_code == HTTPStatus.OK:
        print(f'sucessfully updated {collection_id}/{document_id}')
    else:
        common.handle_http_error(response)


def parse(line):
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    if not args.collection_id:
        raise ValueError('collection_id cannot be null or blank')
    if not args.document_id:
        raise ValueError('document_id cannot be null or blank')    
    return args
    
def execute(client, line):
    if client is None:
        raise ValueError('client is null')
    args = parse(line)
    return exec(client, args.collection_id, args.document_id, args.title, args.source_url, args.metadata, args.mode)
    