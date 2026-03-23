from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Notifications:
    """Notifications management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/notifications", params={k: v for k, v in params.items() if v is not None})

    def mark_read(self, notification_id: str) -> Any:
        return self._client.post(f"/notifications/{notification_id}/read")

    def mark_all_read(self) -> Any:
        return self._client.post("/notifications/read-all")

    def get_preferences(self) -> Any:
        return self._client.get("/notifications/preferences")

    def update_preferences(self, **kwargs: Any) -> Any:
        return self._client.patch(
            "/notifications/preferences", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )


class AsyncNotifications:
    """Notifications management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/notifications", params={k: v for k, v in params.items() if v is not None})

    async def mark_read(self, notification_id: str) -> Any:
        return await self._client.post(f"/notifications/{notification_id}/read")

    async def mark_all_read(self) -> Any:
        return await self._client.post("/notifications/read-all")

    async def get_preferences(self) -> Any:
        return await self._client.get("/notifications/preferences")

    async def update_preferences(self, **kwargs: Any) -> Any:
        return await self._client.patch(
            "/notifications/preferences", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )
