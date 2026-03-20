from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class Backups:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/backups", params={k: v for k, v in params.items() if v is not None})

    def create(self) -> Any:
        return self._client.post("/backups")

    def restore(self, backup_id: str) -> Any:
        return self._client.post(f"/backups/{backup_id}/restore")


class AsyncBackups:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/backups", params={k: v for k, v in params.items() if v is not None})

    async def create(self) -> Any:
        return await self._client.post("/backups")

    async def restore(self, backup_id: str) -> Any:
        return await self._client.post(f"/backups/{backup_id}/restore")
