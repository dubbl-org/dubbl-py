from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class Backups:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/backups", params={k: v for k, v in params.items() if v is not None})

    def create(self) -> ResponseValue:
        return self._client.post("/backups")

    def retrieve(self, backup_id: str) -> ResponseValue:
        return self._client.get(f"/backups/{backup_id}")

    def delete(self, backup_id: str) -> ResponseValue:
        return self._client.delete(f"/backups/{backup_id}")

    def restore(self, backup_id: str) -> ResponseValue:
        return self._client.post(f"/backups/{backup_id}/restore")

    def download(self, backup_id: str) -> ResponseValue:
        return self._client.get(f"/backups/{backup_id}/download", raw_response=True)

    def upload(self, **kwargs: JSONValue) -> ResponseValue:
        body = {k: v for k, v in kwargs.items() if v is not None}
        return self._client.post("/backups/upload", json=body)

    def download_snapshot(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/backups/download-snapshot", params={k: v for k, v in params.items() if v is not None}, raw_response=True
        )


class AsyncBackups:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/backups", params={k: v for k, v in params.items() if v is not None})

    async def create(self) -> ResponseValue:
        return await self._client.post("/backups")

    async def retrieve(self, backup_id: str) -> ResponseValue:
        return await self._client.get(f"/backups/{backup_id}")

    async def delete(self, backup_id: str) -> ResponseValue:
        return await self._client.delete(f"/backups/{backup_id}")

    async def restore(self, backup_id: str) -> ResponseValue:
        return await self._client.post(f"/backups/{backup_id}/restore")

    async def download(self, backup_id: str) -> ResponseValue:
        return await self._client.get(f"/backups/{backup_id}/download", raw_response=True)

    async def upload(self, **kwargs: JSONValue) -> ResponseValue:
        body = {k: v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/backups/upload", json=body)

    async def download_snapshot(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/backups/download-snapshot", params={k: v for k, v in params.items() if v is not None}, raw_response=True
        )
