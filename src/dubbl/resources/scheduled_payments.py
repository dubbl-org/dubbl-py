from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class ScheduledPayments:
    """Manage scheduled payments."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/scheduled-payments", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/scheduled-payments", json=body)

    def retrieve(self, payment_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes scheduled payment update and deletion, but not direct retrieval by id."
        )

    def update(self, payment_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/scheduled-payments/{payment_id}", json=body)

    def delete(self, payment_id: str) -> ResponseValue:
        return self._client.delete(f"/scheduled-payments/{payment_id}")

    def process(self) -> ResponseValue:
        return self._client.post("/scheduled-payments/process")


class AsyncScheduledPayments:
    """Manage scheduled payments (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/scheduled-payments", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/scheduled-payments", json=body)

    async def retrieve(self, payment_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes scheduled payment update and deletion, but not direct retrieval by id."
        )

    async def update(self, payment_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/scheduled-payments/{payment_id}", json=body)

    async def delete(self, payment_id: str) -> ResponseValue:
        return await self._client.delete(f"/scheduled-payments/{payment_id}")

    async def process(self) -> ResponseValue:
        return await self._client.post("/scheduled-payments/process")
