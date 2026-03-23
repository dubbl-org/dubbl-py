from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class AuditLog:
    """Access audit log."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        action: str | None = None,
        entity_type: str | None = None,
    ) -> ResponseValue:
        params: dict[str, JSONValue] = {
            "page": page,
            "limit": limit,
            "action": action,
            "entityType": entity_type,
        }
        return self._client.get("/audit-log", params=params)

    def export(self, **params: QueryValue) -> ResponseValue:
        raise NotImplementedError("The current v1 API does not expose a dedicated audit log export endpoint.")


class AsyncAuditLog:
    """Access audit log (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        action: str | None = None,
        entity_type: str | None = None,
    ) -> ResponseValue:
        params: dict[str, JSONValue] = {
            "page": page,
            "limit": limit,
            "action": action,
            "entityType": entity_type,
        }
        return await self._client.get("/audit-log", params=params)

    async def export(self, **params: QueryValue) -> ResponseValue:
        raise NotImplementedError("The current v1 API does not expose a dedicated audit log export endpoint.")
