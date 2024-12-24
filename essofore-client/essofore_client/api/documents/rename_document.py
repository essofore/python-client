from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.unprocessable_content import UnprocessableContent
from ...types import UNSET, Response


def _get_kwargs(
    *,
    collection_id: str,
    old_id: str,
    new_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["collectionId"] = collection_id

    params["oldId"] = old_id

    params["newId"] = new_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/documents/rename",
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
    old_id: str,
    new_id: str,
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        old_id (str):
        new_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        old_id=old_id,
        new_id=new_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    old_id: str,
    new_id: str,
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        old_id (str):
        new_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, UnprocessableContent]
    """

    return sync_detailed(
        client=client,
        collection_id=collection_id,
        old_id=old_id,
        new_id=new_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    old_id: str,
    new_id: str,
) -> Response[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        old_id (str):
        new_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        old_id=old_id,
        new_id=new_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    old_id: str,
    new_id: str,
) -> Optional[Union[Any, BadRequest, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        old_id (str):
        new_id (str):

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
            old_id=old_id,
            new_id=new_id,
        )
    ).parsed
