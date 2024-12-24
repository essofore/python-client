from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.documents import get_document_info
from essofore_client.models import DocumentInfo
from typing import Any, Dict, List, Optional, Union
from tabulate import tabulate
import shlex

parser = argparse2.ArgumentParser(prog="inspect_document", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('--document_id', required=True)

def exec(client, collection_id, document_id):
    response = get_document_info.sync_detailed(client=client, collection_id=collection_id, document_id=document_id) 
    if response.status_code == HTTPStatus.OK:
        e : DocumentInfo = response.parsed
        header = ['document_id', 'title', 'text', '# of embeddings', 'size']
        all_data = [header]
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
    return exec(client, args.collection_id, args.document_id)
    