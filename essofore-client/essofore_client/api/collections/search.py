from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.search_result import SearchResult
from ...models.unprocessable_content import UnprocessableContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    collection_id: str,
    q: str,
    k: Union[Unset, int] = 5,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["collectionId"] = collection_id

    params["q"] = q

    params["k"] = k

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/collections/query",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, List["SearchResult"], UnprocessableContent]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SearchResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = UnprocessableContent.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequest, List["SearchResult"], UnprocessableContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    q: str,
    k: Union[Unset, int] = 5,
) -> Response[Union[BadRequest, List["SearchResult"], UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        q (str):
        k (Union[Unset, int]):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, List['SearchResult'], UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        q=q,
        k=k,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    q: str,
    k: Union[Unset, int] = 5,
) -> Optional[Union[BadRequest, List["SearchResult"], UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        q (str):
        k (Union[Unset, int]):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, List['SearchResult'], UnprocessableContent]
    """

    return sync_detailed(
        client=client,
        collection_id=collection_id,
        q=q,
        k=k,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    q: str,
    k: Union[Unset, int] = 5,
) -> Response[Union[BadRequest, List["SearchResult"], UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        q (str):
        k (Union[Unset, int]):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, List['SearchResult'], UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        q=q,
        k=k,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    q: str,
    k: Union[Unset, int] = 5,
) -> Optional[Union[BadRequest, List["SearchResult"], UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        q (str):
        k (Union[Unset, int]):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, List['SearchResult'], UnprocessableContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            collection_id=collection_id,
            q=q,
            k=k,
        )
    ).parsed
