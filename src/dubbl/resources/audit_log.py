from __future__ import annotations

from typing import TYPE_CHECKING, Any

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
    ) -> Any:
        params: dict[str, Any] = {
            "page": page,
            "limit": limit,
            "action": action,
            "entityType": entity_type,
        }
        return self._client.get("/audit-log", params=params)

    def export(self, **params: Any) -> Any:
        return self._client.get(
            "/audit-log/export", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )


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
    ) -> Any:
        params: dict[str, Any] = {
            "page": page,
            "limit": limit,
            "action": action,
            "entityType": entity_type,
        }
        return await self._client.get("/audit-log", params=params)

    async def export(self, **params: Any) -> Any:
        return await self._client.get(
            "/audit-log/export", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )
