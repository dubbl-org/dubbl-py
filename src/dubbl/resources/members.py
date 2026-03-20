from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Members:
    """Manage members."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/members", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def invite(self, *, email: str, role: str) -> Any:
        return self._client.post("/members/invite", json={"email": email, "role": role})

    def update(self, member_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/members/{member_id}", json=body)

    def delete(self, member_id: str) -> Any:
        return self._client.delete(f"/members/{member_id}")

    def update_role(self, member_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/members/{member_id}/role", json=body)

    def remove_access(self, member_id: str) -> Any:
        return self._client.post(f"/members/{member_id}/remove-access")


class AsyncMembers:
    """Manage members (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/members", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def invite(self, *, email: str, role: str) -> Any:
        return await self._client.post("/members/invite", json={"email": email, "role": role})

    async def update(self, member_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/members/{member_id}", json=body)

    async def delete(self, member_id: str) -> Any:
        return await self._client.delete(f"/members/{member_id}")

    async def update_role(self, member_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/members/{member_id}/role", json=body)

    async def remove_access(self, member_id: str) -> Any:
        return await self._client.post(f"/members/{member_id}/remove-access")
