from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class DocumentEmails:
    """Document emails management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/document-emails", params={k: v for k, v in params.items() if v is not None})

    def send(self, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes document email listing, preview, and resend, but not direct send."
        )

    def preview(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/document-emails/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve(self, email_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current API lists document emails by documentType and documentId; direct retrieval by email id is"
            " unavailable."
        )

    def resend(self, email_id: str) -> ResponseValue:
        return self._client.post(f"/document-emails/{email_id}/resend")


class AsyncDocumentEmails:
    """Document emails management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/document-emails", params={k: v for k, v in params.items() if v is not None})

    async def send(self, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes document email listing, preview, and resend, but not direct send."
        )

    async def preview(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/document-emails/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, email_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current API lists document emails by documentType and documentId; direct retrieval by email id is"
            " unavailable."
        )

    async def resend(self, email_id: str) -> ResponseValue:
        return await self._client.post(f"/document-emails/{email_id}/resend")
