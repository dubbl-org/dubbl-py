from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class RevenueSchedules:
    """Manage revenue schedules."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get(
            "/revenue-schedules", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/revenue-schedules", json=body)

    def retrieve(self, schedule_id: str) -> Any:
        return self._client.get(f"/revenue-schedules/{schedule_id}")

    def update(self, schedule_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/revenue-schedules/{schedule_id}", json=body)

    def delete(self, schedule_id: str) -> Any:
        return self._client.delete(f"/revenue-schedules/{schedule_id}")

    def recognize(self, schedule_id: str) -> Any:
        return self._client.post(f"/revenue-schedules/{schedule_id}/recognize")


class AsyncRevenueSchedules:
    """Manage revenue schedules (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get(
            "/revenue-schedules", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/revenue-schedules", json=body)

    async def retrieve(self, schedule_id: str) -> Any:
        return await self._client.get(f"/revenue-schedules/{schedule_id}")

    async def update(self, schedule_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/revenue-schedules/{schedule_id}", json=body)

    async def delete(self, schedule_id: str) -> Any:
        return await self._client.delete(f"/revenue-schedules/{schedule_id}")

    async def recognize(self, schedule_id: str) -> Any:
        return await self._client.post(f"/revenue-schedules/{schedule_id}/recognize")
