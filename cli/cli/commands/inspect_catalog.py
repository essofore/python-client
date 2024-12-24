from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.collections import get_catalog_info
from essofore_client.models import CatalogInfo, CatalogEntry
from typing import Any, Dict, List, Optional, Union
from tabulate import tabulate

def exec(client):
    response = get_catalog_info.sync_detailed(client=client) 
    if response.status_code == HTTPStatus.OK:
        catalog : CatalogInfo = response.parsed
        collections : List[CatalogEntry] = catalog.collections
        header = ['collection_id', 'title', '# of documents', '# of embeddings', 'size']
        all_data = [header]
        for e in collections:
            all_data.append([e.collection_id, e.collection_title, common.format_int(e.document_count), common.format_int(e.embeddings_count), common.format_int(e.size)])
        print(tabulate(all_data,headers='firstrow',tablefmt='fancy_grid'))            
    else:
        common.handle_http_error(response)

def execute(client):
    if client is None:
        raise ValueError('client is null')
    return exec(client)
    