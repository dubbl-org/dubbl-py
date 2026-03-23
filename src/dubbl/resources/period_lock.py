from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class PeriodLock:
    """Manage period lock."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> Any:
        return self._client.get("/period-lock")

    def lock(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/period-lock", json=body)

    def update(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch("/period-lock", json=body)

    def unlock(self) -> Any:
        return self._client.delete("/period-lock")


class AsyncPeriodLock:
    """Manage period lock (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> Any:
        return await self._client.get("/period-lock")

    async def lock(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/period-lock", json=body)

    async def update(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch("/period-lock", json=body)

    async def unlock(self) -> Any:
        return await self._client.delete("/period-lock")
