from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.create_collection_metadata import CreateCollectionMetadata
from ...models.unprocessable_content import UnprocessableContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    collection_id: str,
    title: str,
    metadata: Union[Unset, "CreateCollectionMetadata"] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["collectionId"] = collection_id

    params["title"] = title

    json_metadata: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(metadata, Unset):
        json_metadata = metadata.to_dict()
    if not isinstance(json_metadata, Unset):
        params.update(json_metadata)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/collections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
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
    title: str,
    metadata: Union[Unset, "CreateCollectionMetadata"] = UNSET,
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        title (str):
        metadata (Union[Unset, CreateCollectionMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        title=title,
        metadata=metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    title: str,
    metadata: Union[Unset, "CreateCollectionMetadata"] = UNSET,
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        title (str):
        metadata (Union[Unset, CreateCollectionMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, UnprocessableContent]
    """

    return sync_detailed(
        client=client,
        collection_id=collection_id,
        title=title,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    title: str,
    metadata: Union[Unset, "CreateCollectionMetadata"] = UNSET,
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        title (str):
        metadata (Union[Unset, CreateCollectionMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        title=title,
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    title: str,
    metadata: Union[Unset, "CreateCollectionMetadata"] = UNSET,
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        title (str):
        metadata (Union[Unset, CreateCollectionMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, UnprocessableContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            collection_id=collection_id,
            title=title,
            metadata=metadata,
        )
    ).parsed
