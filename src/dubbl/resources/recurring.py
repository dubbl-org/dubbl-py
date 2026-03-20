from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Recurring:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/recurring", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/recurring", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> Any:
        return self._client.get(f"/recurring/{id}")

    def update(self, id: str, **kwargs: Any) -> Any:
        return self._client.patch(f"/recurring/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, id: str) -> Any:
        return self._client.delete(f"/recurring/{id}")


class AsyncRecurring:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/recurring", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post("/recurring", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, id: str) -> Any:
        return await self._client.get(f"/recurring/{id}")

    async def update(self, id: str, **kwargs: Any) -> Any:
        return await self._client.patch(f"/recurring/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def delete(self, id: str) -> Any:
        return await self._client.delete(f"/recurring/{id}")
