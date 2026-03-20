from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class PurchaseOrders:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/purchase-orders", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/purchase-orders", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> Any:
        return self._client.get(f"/purchase-orders/{id}")

    def update(self, id: str, **kwargs: Any) -> Any:
        return self._client.patch(f"/purchase-orders/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, id: str) -> Any:
        return self._client.delete(f"/purchase-orders/{id}")

    def counts(self, **params: Any) -> Any:
        return self._client.get("/purchase-orders/counts", params={k: v for k, v in params.items() if v is not None})

    def send(self, order_id: str) -> Any:
        return self._client.post(f"/purchase-orders/{order_id}/send")

    def convert(self, order_id: str) -> Any:
        return self._client.post(f"/purchase-orders/{order_id}/convert")


class AsyncPurchaseOrders:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/purchase-orders", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post("/purchase-orders", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, id: str) -> Any:
        return await self._client.get(f"/purchase-orders/{id}")

    async def update(self, id: str, **kwargs: Any) -> Any:
        return await self._client.patch(f"/purchase-orders/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def delete(self, id: str) -> Any:
        return await self._client.delete(f"/purchase-orders/{id}")

    async def counts(self, **params: Any) -> Any:
        return await self._client.get("/purchase-orders/counts", params={k: v for k, v in params.items() if v is not None})

    async def send(self, order_id: str) -> Any:
        return await self._client.post(f"/purchase-orders/{order_id}/send")

    async def convert(self, order_id: str) -> Any:
        return await self._client.post(f"/purchase-orders/{order_id}/convert")
