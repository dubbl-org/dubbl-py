from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class DocumentEmails:
    """Document emails management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/document-emails", params={k: v for k, v in params.items() if v is not None})

    def send(self, **kwargs: Any) -> Any:
        return self._client.post("/document-emails", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def preview(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/document-emails/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve(self, email_id: str) -> Any:
        return self._client.get(f"/document-emails/{email_id}")

    def resend(self, email_id: str) -> Any:
        return self._client.post(f"/document-emails/{email_id}/resend")


class AsyncDocumentEmails:
    """Document emails management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/document-emails", params={k: v for k, v in params.items() if v is not None})

    async def send(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/document-emails", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/document-emails/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, email_id: str) -> Any:
        return await self._client.get(f"/document-emails/{email_id}")

    async def resend(self, email_id: str) -> Any:
        return await self._client.post(f"/document-emails/{email_id}/resend")
