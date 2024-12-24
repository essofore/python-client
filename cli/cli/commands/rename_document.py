from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.documents import rename_document
import shlex

# exit_on_error is broken. see: https://github.com/python/cpython/issues/85427
parser = argparse2.ArgumentParser(prog="rename_document", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('--old_id', required=True)
parser.add_argument('--new_id', required=True)

def exec(client, collection_id, old_id, new_id):        
    response = rename_document.sync_detailed(collection_id=collection_id, old_id=old_id, new_id=new_id, client=client)
    if response.status_code == HTTPStatus.OK:
        print(f'sucessfully renamed {old_id} to {new_id}')
    else:
        common.handle_http_error(response)

def execute(client, line):
    if client is None:
        raise ValueError('client is null')
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    collection_id = args.collection_id
    old_id = args.old_id
    new_id = args.new_id
    return exec(client, collection_id, old_id, new_id)
    