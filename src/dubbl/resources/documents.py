from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Documents:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/documents", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/documents", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> Any:
        return self._client.get(f"/documents/{id}")

    def update(self, id: str, **kwargs: Any) -> Any:
        return self._client.patch(f"/documents/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, id: str) -> Any:
        return self._client.delete(f"/documents/{id}")

    def download(self, id: str) -> Any:
        return self._client.get(f"/documents/{id}/download", raw_response=True)

    def list_folders(self, **params: Any) -> Any:
        return self._client.get("/documents/folders", params={k: v for k, v in params.items() if v is not None})

    def create_folder(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/documents/folders", json=body)

    def retrieve_folder(self, id: str) -> Any:
        return self._client.get(f"/documents/folders/{id}")

    def update_folder(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/documents/folders/{id}", json=body)

    def delete_folder(self, id: str) -> Any:
        return self._client.delete(f"/documents/folders/{id}")


class AsyncDocuments:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/documents", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post("/documents", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, id: str) -> Any:
        return await self._client.get(f"/documents/{id}")

    async def update(self, id: str, **kwargs: Any) -> Any:
        return await self._client.patch(f"/documents/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def delete(self, id: str) -> Any:
        return await self._client.delete(f"/documents/{id}")

    async def download(self, id: str) -> Any:
        return await self._client.get(f"/documents/{id}/download", raw_response=True)

    async def list_folders(self, **params: Any) -> Any:
        return await self._client.get("/documents/folders", params={k: v for k, v in params.items() if v is not None})

    async def create_folder(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/documents/folders", json=body)

    async def retrieve_folder(self, id: str) -> Any:
        return await self._client.get(f"/documents/folders/{id}")

    async def update_folder(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/documents/folders/{id}", json=body)

    async def delete_folder(self, id: str) -> Any:
        return await self._client.delete(f"/documents/folders/{id}")
