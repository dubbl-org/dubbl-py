from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Webhooks:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/webhooks", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post("/webhooks", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> ResponseValue:
        return self._client.get(f"/webhooks/{id}")

    def update(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(f"/webhooks/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, id: str) -> ResponseValue:
        return self._client.delete(f"/webhooks/{id}")

    def subscribe(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/webhooks/subscribe", json=body)

    def unsubscribe(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/webhooks/unsubscribe", json=body)

    def list_deliveries(self, webhook_id: str) -> ResponseValue:
        return self._client.get(f"/webhooks/{webhook_id}/deliveries")

    def test(self, webhook_id: str) -> ResponseValue:
        return self._client.post(f"/webhooks/{webhook_id}/test")


class AsyncWebhooks:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/webhooks", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post("/webhooks", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, id: str) -> ResponseValue:
        return await self._client.get(f"/webhooks/{id}")

    async def update(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/webhooks/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, id: str) -> ResponseValue:
        return await self._client.delete(f"/webhooks/{id}")

    async def subscribe(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/webhooks/subscribe", json=body)

    async def unsubscribe(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/webhooks/unsubscribe", json=body)

    async def list_deliveries(self, webhook_id: str) -> ResponseValue:
        return await self._client.get(f"/webhooks/{webhook_id}/deliveries")

    async def test(self, webhook_id: str) -> ResponseValue:
        return await self._client.post(f"/webhooks/{webhook_id}/test")
