from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.collections import create_collection
from essofore_client.models.create_collection_metadata import CreateCollectionMetadata
import shlex

# exit_on_error is broken. see: https://github.com/python/cpython/issues/85427
parser = argparse2.ArgumentParser(prog="create_collection", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('--title', nargs='+', required=True)
parser.add_argument('--metadata', nargs='+', action=argparse2.ParseKeyValuePairs, help='metadata expressed as key=value pairs', required=False, default={})

def exec(client, id, title, metadata):
    if metadata is not None:
        metadata = CreateCollectionMetadata.from_dict(metadata)
    response = create_collection.sync_detailed(collection_id=id, title=title, metadata=metadata, client=client)
    if response.status_code == HTTPStatus.OK:
        print(f'successfully created {id}')
    else:
        common.handle_http_error(response)

def execute(client, line):
    """
        create collection --collection_id 3 --title "Effective Java" --metadata "author=Joshua Bloch" "publisher=Pearson Addison-Wesley"        
    """
    if client is None:
        raise ValueError('client is null')
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    id = args.collection_id
    if not args.title or len(args.title) == 0:
        raise ValueError('title cannot be empty')
    title = ' '.join(args.title)
    if not id:
        raise ValueError('id cannot be empty')
    if not title:
        raise ValueError('title cannot be empty')
    return exec(client, id, title, args.metadata)
    