from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Teams:
    """Manage teams."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/teams", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/teams", json=body)

    def retrieve(self, team_id: str) -> Any:
        return self._client.get(f"/teams/{team_id}")

    def update(self, team_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/teams/{team_id}", json=body)

    def delete(self, team_id: str) -> Any:
        return self._client.delete(f"/teams/{team_id}")

    def list_members(self, team_id: str) -> Any:
        return self._client.get(f"/teams/{team_id}/members")

    def add_member(self, team_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/teams/{team_id}/members", json=body)

    def remove_member(self, team_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.delete(f"/teams/{team_id}/members", json=body)


class AsyncTeams:
    """Manage teams (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/teams", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/teams", json=body)

    async def retrieve(self, team_id: str) -> Any:
        return await self._client.get(f"/teams/{team_id}")

    async def update(self, team_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/teams/{team_id}", json=body)

    async def delete(self, team_id: str) -> Any:
        return await self._client.delete(f"/teams/{team_id}")

    async def list_members(self, team_id: str) -> Any:
        return await self._client.get(f"/teams/{team_id}/members")

    async def add_member(self, team_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/teams/{team_id}/members", json=body)

    async def remove_member(self, team_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.delete(f"/teams/{team_id}/members", json=body)
