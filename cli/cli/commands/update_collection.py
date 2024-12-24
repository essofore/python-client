from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.collections import update_collection
from essofore_client.models.update_collection_metadata import UpdateCollectionMetadata
from essofore_client.models.metadata_mode import MetadataMode
import shlex

# exit_on_error is broken. see: https://github.com/python/cpython/issues/85427
parser = argparse2.ArgumentParser(prog="update_document", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('--title', nargs='+', required=False)
parser.add_argument('--metadata', nargs='+', action=argparse2.ParseKeyValuePairs, help='metadata expressed as key=value pairs', required=False, default={})
parser.add_argument('--mode', required=False, choices=['update', 'replace'], default='update')

def exec(client, collection_id, title, metadata, mode):
    if metadata is not None:
        metadata = UpdateCollectionMetadata.from_dict(metadata)
    # upper needed to fix Caused by: java.lang.IllegalArgumentException: No enum constant essofore.openapi.model.MetadataMode.update
	#                                   at java.base/java.lang.Enum.valueOf(Enum.java:293) ~[na:na]
    response = update_collection.sync_detailed(collection_id=collection_id, title=title, metadata=metadata, merge=MetadataMode(mode.upper()), client=client)
    if response.status_code == HTTPStatus.OK:
        print(f'sucessfully updated {collection_id}')
    else:
        common.handle_http_error(response)


def parse(line):
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    if not args.collection_id:
        raise ValueError('collection_id cannot be null or blank')
    return args
    
def execute(client, line):
    """
        update collection --collection_id 1 --metadata "author=Joshua Bloch" "publisher=Pearson Addison-Wesley"
    """
    if client is None:
        raise ValueError('client is null')
    args = parse(line)
    return exec(client, args.collection_id, args.title, args.metadata, args.mode)
    