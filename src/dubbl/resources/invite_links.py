from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class InviteLinks:
    """Manage invite links."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/invite-links", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/invite-links", json=body)

    def retrieve(self, link_id: str) -> Any:
        return self._client.get(f"/invite-links/{link_id}")

    def update(self, link_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/invite-links/{link_id}", json=body)

    def delete(self, link_id: str) -> Any:
        return self._client.delete(f"/invite-links/{link_id}")

    def get_info(self, **params: Any) -> Any:
        return self._client.get("/invite-links/info", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def join(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/invite-links/join", json=body)


class AsyncInviteLinks:
    """Manage invite links (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/invite-links", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/invite-links", json=body)

    async def retrieve(self, link_id: str) -> Any:
        return await self._client.get(f"/invite-links/{link_id}")

    async def update(self, link_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/invite-links/{link_id}", json=body)

    async def delete(self, link_id: str) -> Any:
        return await self._client.delete(f"/invite-links/{link_id}")

    async def get_info(self, **params: Any) -> Any:
        return await self._client.get("/invite-links/info", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def join(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/invite-links/join", json=body)
