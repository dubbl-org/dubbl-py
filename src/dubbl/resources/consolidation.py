from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Consolidation:
    """Consolidation groups management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/consolidation/groups", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/consolidation/groups", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, group_id: str) -> Any:
        return self._client.get(f"/consolidation/groups/{group_id}")

    def update(self, group_id: str, **kwargs: Any) -> Any:
        return self._client.patch(f"/consolidation/groups/{group_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, group_id: str) -> Any:
        return self._client.delete(f"/consolidation/groups/{group_id}")

    def list_members(self, group_id: str) -> Any:
        return self._client.get(f"/consolidation/groups/{group_id}/members")

    def add_member(self, group_id: str, **kwargs: Any) -> Any:
        return self._client.post(f"/consolidation/groups/{group_id}/members", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def remove_member(self, group_id: str, **kwargs: Any) -> Any:
        return self._client.post(f"/consolidation/groups/{group_id}/members/remove", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def get_report(self, group_id: str, **params: Any) -> Any:
        return self._client.get(f"/consolidation/groups/{group_id}/report", params={k: v for k, v in params.items() if v is not None})


class AsyncConsolidation:
    """Consolidation groups management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/consolidation/groups", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post("/consolidation/groups", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, group_id: str) -> Any:
        return await self._client.get(f"/consolidation/groups/{group_id}")

    async def update(self, group_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(f"/consolidation/groups/{group_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def delete(self, group_id: str) -> Any:
        return await self._client.delete(f"/consolidation/groups/{group_id}")

    async def list_members(self, group_id: str) -> Any:
        return await self._client.get(f"/consolidation/groups/{group_id}/members")

    async def add_member(self, group_id: str, **kwargs: Any) -> Any:
        return await self._client.post(f"/consolidation/groups/{group_id}/members", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def remove_member(self, group_id: str, **kwargs: Any) -> Any:
        return await self._client.post(f"/consolidation/groups/{group_id}/members/remove", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def get_report(self, group_id: str, **params: Any) -> Any:
        return await self._client.get(f"/consolidation/groups/{group_id}/report", params={k: v for k, v in params.items() if v is not None})
