from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.unprocessable_content import UnprocessableContent
from ...types import Response


def _get_kwargs(
    collection_id: str,
    document_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/documents/{collection_id}/{document_id}",
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
    collection_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        document_id=document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, UnprocessableContent]
    """

    return sync_detailed(
        collection_id=collection_id,
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        document_id=document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, UnprocessableContent]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            document_id=document_id,
            client=client,
        )
    ).parsed
