from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class Trash:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/trash", params={k: v for k, v in params.items() if v is not None})

    def restore(self, item_id: str) -> Any:
        return self._client.post(f"/trash/{item_id}/restore")

    def permanent_delete(self, id: str) -> Any:
        return self._client.delete(f"/trash/{id}")

    def empty(self) -> Any:
        return self._client.post("/trash/empty")


class AsyncTrash:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/trash", params={k: v for k, v in params.items() if v is not None})

    async def restore(self, item_id: str) -> Any:
        return await self._client.post(f"/trash/{item_id}/restore")

    async def permanent_delete(self, id: str) -> Any:
        return await self._client.delete(f"/trash/{id}")

    async def empty(self) -> Any:
        return await self._client.post("/trash/empty")
