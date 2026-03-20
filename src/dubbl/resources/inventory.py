from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Inventory:
    """Manage inventory."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        search: Optional[str] = None,
        category: Optional[str] = None,
        category_id: Optional[str] = None,
        status: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Any:
        params: Dict[str, Any] = {
            "search": search,
            "category": category,
            "categoryId": category_id,
            "status": status,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "page": page,
            "limit": limit,
        }
        return self._client.get("/inventory", params=params)

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory", json=body)

    def retrieve(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}")

    def update(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/{item_id}", json=body)

    def delete(self, item_id: str) -> Any:
        return self._client.delete(f"/inventory/{item_id}")

    def list_categories(self) -> Any:
        return self._client.get("/inventory/categories")

    def create_category(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/categories", json=body)

    def list_stock_takes(self) -> Any:
        return self._client.get("/inventory/stock-takes")

    def create_stock_take(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/stock-takes", json=body)

    def adjust_stock_take(self, stock_take_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/stock-takes/{stock_take_id}/adjust", json=body)

    def list_assemblies(self) -> Any:
        return self._client.get("/inventory/assemblies")

    def create_assembly(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/assemblies", json=body)


class AsyncInventory:
    """Manage inventory (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        search: Optional[str] = None,
        category: Optional[str] = None,
        category_id: Optional[str] = None,
        status: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Any:
        params: Dict[str, Any] = {
            "search": search,
            "category": category,
            "categoryId": category_id,
            "status": status,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "page": page,
            "limit": limit,
        }
        return await self._client.get("/inventory", params=params)

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory", json=body)

    async def retrieve(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}")

    async def update(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/{item_id}", json=body)

    async def delete(self, item_id: str) -> Any:
        return await self._client.delete(f"/inventory/{item_id}")

    async def list_categories(self) -> Any:
        return await self._client.get("/inventory/categories")

    async def create_category(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/categories", json=body)

    async def list_stock_takes(self) -> Any:
        return await self._client.get("/inventory/stock-takes")

    async def create_stock_take(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/stock-takes", json=body)

    async def adjust_stock_take(self, stock_take_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/stock-takes/{stock_take_id}/adjust", json=body)

    async def list_assemblies(self) -> Any:
        return await self._client.get("/inventory/assemblies")

    async def create_assembly(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/assemblies", json=body)
