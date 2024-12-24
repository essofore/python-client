from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.document_info import DocumentInfo
from ...models.document_type import DocumentType
from ...models.download_document_metadata import DownloadDocumentMetadata
from ...models.unprocessable_content import UnprocessableContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    collection_id: str,
    document_id: str,
    title: str,
    doc_type: DocumentType,
    source_url: str,
    metadata: Union[Unset, "DownloadDocumentMetadata"] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["collectionId"] = collection_id

    params["documentId"] = document_id

    params["title"] = title

    json_doc_type = doc_type.value
    params["docType"] = json_doc_type

    params["sourceUrl"] = source_url

    json_metadata: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(metadata, Unset):
        json_metadata = metadata.to_dict()
    if not isinstance(json_metadata, Unset):
        params.update(json_metadata)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/documents/download",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, DocumentInfo, UnprocessableContent]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DocumentInfo.from_dict(response.json())

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
) -> Response[Union[BadRequest, DocumentInfo, UnprocessableContent]]:
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
    document_id: str,
    title: str,
    doc_type: DocumentType,
    source_url: str,
    metadata: Union[Unset, "DownloadDocumentMetadata"] = UNSET,
) -> Response[Union[BadRequest, DocumentInfo, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):
        title (str):
        doc_type (DocumentType):
        source_url (str):
        metadata (Union[Unset, DownloadDocumentMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, DocumentInfo, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        document_id=document_id,
        title=title,
        doc_type=doc_type,
        source_url=source_url,
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
    document_id: str,
    title: str,
    doc_type: DocumentType,
    source_url: str,
    metadata: Union[Unset, "DownloadDocumentMetadata"] = UNSET,
) -> Optional[Union[BadRequest, DocumentInfo, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):
        title (str):
        doc_type (DocumentType):
        source_url (str):
        metadata (Union[Unset, DownloadDocumentMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, DocumentInfo, UnprocessableContent]
    """

    return sync_detailed(
        client=client,
        collection_id=collection_id,
        document_id=document_id,
        title=title,
        doc_type=doc_type,
        source_url=source_url,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    document_id: str,
    title: str,
    doc_type: DocumentType,
    source_url: str,
    metadata: Union[Unset, "DownloadDocumentMetadata"] = UNSET,
) -> Response[Union[BadRequest, DocumentInfo, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):
        title (str):
        doc_type (DocumentType):
        source_url (str):
        metadata (Union[Unset, DownloadDocumentMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, DocumentInfo, UnprocessableContent]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        document_id=document_id,
        title=title,
        doc_type=doc_type,
        source_url=source_url,
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    collection_id: str,
    document_id: str,
    title: str,
    doc_type: DocumentType,
    source_url: str,
    metadata: Union[Unset, "DownloadDocumentMetadata"] = UNSET,
) -> Optional[Union[BadRequest, DocumentInfo, UnprocessableContent]]:
    """
    Args:
        collection_id (str):
        document_id (str):
        title (str):
        doc_type (DocumentType):
        source_url (str):
        metadata (Union[Unset, DownloadDocumentMetadata]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, DocumentInfo, UnprocessableContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            collection_id=collection_id,
            document_id=document_id,
            title=title,
            doc_type=doc_type,
            source_url=source_url,
            metadata=metadata,
        )
    ).parsed
