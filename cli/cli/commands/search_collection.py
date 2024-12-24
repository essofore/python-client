from . import argparse2
from . import common
from http import HTTPStatus
from essofore_client.api.collections import search
from essofore_client.models import SearchResult
from typing import Any, Dict, List, Optional, Union
import shlex

def parse_k(k : str) -> int:
    ivalue = int(k)
    if ivalue <= 0:
        raise ValueError("%s is an invalid positive integer value" % k)
    if ivalue > 10:
        raise ValueError("%s is an invalid value, should be less than or equal to 10" % k)
    return ivalue

# exit_on_error is broken. see: https://github.com/python/cpython/issues/85427
parser = argparse2.ArgumentParser(prog="search_collection", exit_on_error=False)
parser.add_argument('--collection_id', required=True)
parser.add_argument('-q', '--query', required=True, nargs='+')

# The argument to type can be any callable that accepts a single string.
# If the function raises ArgumentTypeError, TypeError, or ValueError, the exception is caught and a nicely formatted error message is displayed. No other exception types are handled.
parser.add_argument('-k', default=5, type=parse_k)

def print_search_result(i: int, r : SearchResult):
    header = f"{i}. {r.title}"
    print(header)
    print('-' * len(header))
    print(r.text)
    print('\n')

def exec(client, collection_id, query, k):
    response = search.sync_detailed(client=client, collection_id=collection_id, q=query, k=k)                         
    if response.status_code == HTTPStatus.OK:
        results : List[SearchResult] = response.parsed
        if results:
            i = 1
            for r in results:
                print_search_result(i, r)
                i += 1
        else:
            print('query returned with no results')
    else:
        common.handle_http_error(response)

def validate(line):
    if line is None:
        raise ValueError('line is null')
    args = parser.parse_args(shlex.split(line))
    if not args.collection_id:
        raise ValueError('collection_id cannot be null or blank')
    if not args.query or len(args.query) == 0:
        raise ValueError('query cannot be empty')
    args.query = ' '.join(args.query)
    if not args.query:
        raise ValueError('query cannot be empty')
    if not args.k or args.k <= 0 or args.k > 10:
        raise ValueError('k must be between 1 and 10 (inclusive)')
    return args

def execute(client, line):
    if client is None:
        raise ValueError('client is null')
    args = validate(line)
    return exec(client, args.collection_id, args.query, args.k)
    