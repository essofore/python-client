from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.collections import get_collection_info
from essofore_client.models import CollectionInfo, DocumentInfo
from typing import Any, Dict, List, Optional, Union
from tabulate import tabulate
import shlex

parser = argparse2.ArgumentParser(prog="inspect_collection", exit_on_error=False)
parser.add_argument('--collection_id', required=True)

def exec(client, collection_id):
    response = get_collection_info.sync_detailed(client=client, collection_id=collection_id) 
    if response.status_code == HTTPStatus.OK:
        col_info : CollectionInfo = response.parsed
        documents : List[DocumentInfo] = col_info.documents
        header = ['document_id', 'title', 'text', '# of embeddings', 'size']
        all_data = [header]
        for e in documents:
            all_data.append([e.document_id, e.title, e.sample_text, common.format_int(e.embeddings_count), common.format_int(e.size)])
        print(tabulate(all_data,headers='firstrow',tablefmt='fancy_grid'))
    else:
        common.handle_http_error(response)

def execute(client, line):
    if client is None:
        raise ValueError('client is null')
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    return exec(client, args.collection_id)
    