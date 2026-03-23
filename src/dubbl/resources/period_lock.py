from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class PeriodLock:
    """Manage period lock."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> ResponseValue:
        return self._client.get("/period-lock")

    def lock(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.put("/period-lock", json=body)

    def update(self, **kwargs: JSONValue) -> ResponseValue:
        return self.lock(**kwargs)

    def unlock(self) -> ResponseValue:
        raise NotImplementedError("The current v1 API exposes period lock upsert via PUT, but not unlock/delete.")


class AsyncPeriodLock:
    """Manage period lock (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> ResponseValue:
        return await self._client.get("/period-lock")

    async def lock(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.put("/period-lock", json=body)

    async def update(self, **kwargs: JSONValue) -> ResponseValue:
        return await self.lock(**kwargs)

    async def unlock(self) -> ResponseValue:
        raise NotImplementedError("The current v1 API exposes period lock upsert via PUT, but not unlock/delete.")
