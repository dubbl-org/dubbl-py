from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Warehouses:
    """Manage warehouses."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/warehouses", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/warehouses", json=body)

    def retrieve(self, warehouse_id: str) -> ResponseValue:
        return self._client.get(f"/warehouses/{warehouse_id}")

    def update(self, warehouse_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/warehouses/{warehouse_id}", json=body)

    def delete(self, warehouse_id: str) -> ResponseValue:
        return self._client.delete(f"/warehouses/{warehouse_id}")

    def get_stock(self, warehouse_id: str) -> ResponseValue:
        return self._client.get(f"/warehouses/{warehouse_id}/stock")

    def update_stock(self, warehouse_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes warehouse stock retrieval, but not direct stock updates."
        )


class AsyncWarehouses:
    """Manage warehouses (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/warehouses", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/warehouses", json=body)

    async def retrieve(self, warehouse_id: str) -> ResponseValue:
        return await self._client.get(f"/warehouses/{warehouse_id}")

    async def update(self, warehouse_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/warehouses/{warehouse_id}", json=body)

    async def delete(self, warehouse_id: str) -> ResponseValue:
        return await self._client.delete(f"/warehouses/{warehouse_id}")

    async def get_stock(self, warehouse_id: str) -> ResponseValue:
        return await self._client.get(f"/warehouses/{warehouse_id}/stock")

    async def update_stock(self, warehouse_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes warehouse stock retrieval, but not direct stock updates."
        )
