from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class ReportSchedules:
    """Manage report schedules."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/report-schedules", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/report-schedules", json=body)

    def retrieve(self, schedule_id: str) -> ResponseValue:
        return self._client.get(f"/report-schedules/{schedule_id}")

    def update(self, schedule_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/report-schedules/{schedule_id}", json=body)

    def delete(self, schedule_id: str) -> ResponseValue:
        return self._client.delete(f"/report-schedules/{schedule_id}")


class AsyncReportSchedules:
    """Manage report schedules (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/report-schedules", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/report-schedules", json=body)

    async def retrieve(self, schedule_id: str) -> ResponseValue:
        return await self._client.get(f"/report-schedules/{schedule_id}")

    async def update(self, schedule_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/report-schedules/{schedule_id}", json=body)

    async def delete(self, schedule_id: str) -> ResponseValue:
        return await self._client.delete(f"/report-schedules/{schedule_id}")
