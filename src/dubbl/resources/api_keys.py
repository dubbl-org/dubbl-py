from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class ApiKeys:
    """Manage API keys."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self) -> Any:
        return self._client.get("/api-keys")

    def create(self, *, name: str, expires_at: Optional[str] = None) -> Any:
        body: Dict[str, Any] = {"name": name, "expiresAt": expires_at}
        return self._client.post("/api-keys", json={k: v for k, v in body.items() if v is not None})

    def delete(self, key_id: str) -> Any:
        return self._client.delete(f"/api-keys/{key_id}")


class AsyncApiKeys:
    """Manage API keys (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self) -> Any:
        return await self._client.get("/api-keys")

    async def create(self, *, name: str, expires_at: Optional[str] = None) -> Any:
        body: Dict[str, Any] = {"name": name, "expiresAt": expires_at}
        return await self._client.post("/api-keys", json={k: v for k, v in body.items() if v is not None})

    async def delete(self, key_id: str) -> Any:
        return await self._client.delete(f"/api-keys/{key_id}")
