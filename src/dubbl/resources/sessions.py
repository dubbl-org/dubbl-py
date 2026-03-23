from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Sessions:
    """Manage sessions."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/sessions", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def delete(self, session_id: str) -> ResponseValue:
        raise NotImplementedError("The current API no longer supports revoking individual sessions; use revoke_all().")

    def revoke_all(self) -> ResponseValue:
        return self._client.post("/sessions/revoke-all")


class AsyncSessions:
    """Manage sessions (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/sessions", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def delete(self, session_id: str) -> ResponseValue:
        raise NotImplementedError("The current API no longer supports revoking individual sessions; use revoke_all().")

    async def revoke_all(self) -> ResponseValue:
        return await self._client.post("/sessions/revoke-all")
