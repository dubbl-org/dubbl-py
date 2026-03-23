from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Reminders:
    """Manage reminders."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/reminders", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/reminders", json=body)

    def retrieve(self, reminder_id: str) -> ResponseValue:
        return self._client.get(f"/reminders/{reminder_id}")

    def update(self, reminder_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.put(f"/reminders/{reminder_id}", json=body)

    def delete(self, reminder_id: str) -> ResponseValue:
        return self._client.delete(f"/reminders/{reminder_id}")

    def get_logs(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/reminders/logs", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def process(self) -> ResponseValue:
        return self._client.post("/reminders/process")


class AsyncReminders:
    """Manage reminders (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/reminders", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/reminders", json=body)

    async def retrieve(self, reminder_id: str) -> ResponseValue:
        return await self._client.get(f"/reminders/{reminder_id}")

    async def update(self, reminder_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.put(f"/reminders/{reminder_id}", json=body)

    async def delete(self, reminder_id: str) -> ResponseValue:
        return await self._client.delete(f"/reminders/{reminder_id}")

    async def get_logs(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/reminders/logs", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def process(self) -> ResponseValue:
        return await self._client.post("/reminders/process")
