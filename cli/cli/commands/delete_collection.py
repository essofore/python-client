from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.collections import delete_collection
import shlex

parser = argparse2.ArgumentParser(prog="delete_collection", exit_on_error=False)
parser.add_argument('--collection_id', required=True)

def exec(client, collection_id):
    response = delete_collection.sync_detailed(client=client, collection_id=collection_id) 
    if response.status_code == HTTPStatus.OK:
        print(f'successfully deleted {collection_id}')
    else:
        common.handle_http_error(response)

def execute(client, line):
    if client is None:
        raise ValueError('client is null')
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    return exec(client, args.collection_id)
    