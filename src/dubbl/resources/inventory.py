from __future__ import annotations

from typing import TYPE_CHECKING, Any

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
        search: str | None = None,
        category: str | None = None,
        category_id: str | None = None,
        status: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Any:
        params: dict[str, Any] = {
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

    def retrieve_category(self, category_id: str) -> Any:
        return self._client.get(f"/inventory/categories/{category_id}")

    def update_category(self, category_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/categories/{category_id}", json=body)

    def delete_category(self, category_id: str) -> Any:
        return self._client.delete(f"/inventory/categories/{category_id}")

    def list_stock_takes(self) -> Any:
        return self._client.get("/stock-takes")

    def create_stock_take(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/stock-takes", json=body)

    def adjust_stock_take(self, stock_take_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/stock-takes/{stock_take_id}", json=body)

    def list_assemblies(self) -> Any:
        return self._client.get("/inventory/assembly-orders")

    def create_assembly(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/assembly-orders", json=body)

    # Item-level operations
    def adjust(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/{item_id}/adjust", json=body)

    def list_lots(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/lots")

    def add_lot(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/{item_id}/lots", json=body)

    def list_serials(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/serials")

    def add_serial(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/{item_id}/serials", json=body)

    def list_movements(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/movements")

    def list_variants(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/variants")

    def create_variant(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/{item_id}/variants", json=body)

    def retrieve_variant(self, item_id: str, variant_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/variants/{variant_id}")

    def update_variant(self, item_id: str, variant_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/{item_id}/variants/{variant_id}", json=body)

    def delete_variant(self, item_id: str, variant_id: str) -> Any:
        return self._client.delete(f"/inventory/{item_id}/variants/{variant_id}")

    def list_suppliers(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/suppliers")

    def add_supplier(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/{item_id}/suppliers", json=body)

    def update_supplier(self, item_id: str, supplier_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/{item_id}/suppliers/{supplier_id}", json=body)

    def delete_supplier(self, item_id: str, supplier_id: str) -> Any:
        return self._client.delete(f"/inventory/{item_id}/suppliers/{supplier_id}")

    def get_warehouse_stock(self, item_id: str) -> Any:
        return self._client.get(f"/inventory/{item_id}/warehouse-stock")

    # Bulk operations
    def import_items(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/import", json=body)

    def bulk_operations(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/bulk", json=body)

    def get_reorder_suggestions(self) -> Any:
        return self._client.get("/inventory/reorder-suggestions")

    def get_movements_chart(self, **params: Any) -> Any:
        return self._client.get(
            "/inventory/movements/chart", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    # Transfers
    def list_transfers(self, **params: Any) -> Any:
        return self._client.get(
            "/inventory/transfers", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create_transfer(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/transfers", json=body)

    def retrieve_transfer(self, id: str) -> Any:
        return self._client.get(f"/inventory/transfers/{id}")

    def update_transfer(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/transfers/{id}", json=body)

    def delete_transfer(self, id: str) -> Any:
        return self._client.delete(f"/inventory/transfers/{id}")

    def complete_transfer(self, id: str) -> Any:
        return self._client.post(f"/inventory/transfers/{id}/complete")

    # BOMs
    def list_bom(self, **params: Any) -> Any:
        return self._client.get("/inventory/bom", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create_bom(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/bom", json=body)

    def retrieve_bom(self, id: str) -> Any:
        return self._client.get(f"/inventory/bom/{id}")

    def update_bom(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/bom/{id}", json=body)

    def delete_bom(self, id: str) -> Any:
        return self._client.delete(f"/inventory/bom/{id}")

    def list_bom_components(self, bom_id: str) -> Any:
        return self._client.get(f"/inventory/bom/{bom_id}/components")

    def add_bom_component(self, bom_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/inventory/bom/{bom_id}/components", json=body)

    def delete_bom_component(self, bom_id: str, component_id: str) -> Any:
        return self._client.delete(f"/inventory/bom/{bom_id}/components/{component_id}")

    # Assembly orders
    def list_assembly_orders(self, **params: Any) -> Any:
        return self._client.get(
            "/inventory/assembly-orders", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create_assembly_order(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/inventory/assembly-orders", json=body)

    def retrieve_assembly_order(self, id: str) -> Any:
        return self._client.get(f"/inventory/assembly-orders/{id}")

    def update_assembly_order(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/inventory/assembly-orders/{id}", json=body)

    def delete_assembly_order(self, id: str) -> Any:
        return self._client.delete(f"/inventory/assembly-orders/{id}")

    def complete_assembly_order(self, id: str) -> Any:
        return self._client.post(f"/inventory/assembly-orders/{id}/complete")


class AsyncInventory:
    """Manage inventory (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        search: str | None = None,
        category: str | None = None,
        category_id: str | None = None,
        status: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Any:
        params: dict[str, Any] = {
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

    async def retrieve_category(self, category_id: str) -> Any:
        return await self._client.get(f"/inventory/categories/{category_id}")

    async def update_category(self, category_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/categories/{category_id}", json=body)

    async def delete_category(self, category_id: str) -> Any:
        return await self._client.delete(f"/inventory/categories/{category_id}")

    async def list_stock_takes(self) -> Any:
        return await self._client.get("/stock-takes")

    async def create_stock_take(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/stock-takes", json=body)

    async def adjust_stock_take(self, stock_take_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/stock-takes/{stock_take_id}", json=body)

    async def list_assemblies(self) -> Any:
        return await self._client.get("/inventory/assembly-orders")

    async def create_assembly(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/assembly-orders", json=body)

    # Item-level operations
    async def adjust(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/{item_id}/adjust", json=body)

    async def list_lots(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/lots")

    async def add_lot(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/{item_id}/lots", json=body)

    async def list_serials(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/serials")

    async def add_serial(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/{item_id}/serials", json=body)

    async def list_movements(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/movements")

    async def list_variants(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/variants")

    async def create_variant(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/{item_id}/variants", json=body)

    async def retrieve_variant(self, item_id: str, variant_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/variants/{variant_id}")

    async def update_variant(self, item_id: str, variant_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/{item_id}/variants/{variant_id}", json=body)

    async def delete_variant(self, item_id: str, variant_id: str) -> Any:
        return await self._client.delete(f"/inventory/{item_id}/variants/{variant_id}")

    async def list_suppliers(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/suppliers")

    async def add_supplier(self, item_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/{item_id}/suppliers", json=body)

    async def update_supplier(self, item_id: str, supplier_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/{item_id}/suppliers/{supplier_id}", json=body)

    async def delete_supplier(self, item_id: str, supplier_id: str) -> Any:
        return await self._client.delete(f"/inventory/{item_id}/suppliers/{supplier_id}")

    async def get_warehouse_stock(self, item_id: str) -> Any:
        return await self._client.get(f"/inventory/{item_id}/warehouse-stock")

    # Bulk operations
    async def import_items(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/import", json=body)

    async def bulk_operations(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/bulk", json=body)

    async def get_reorder_suggestions(self) -> Any:
        return await self._client.get("/inventory/reorder-suggestions")

    async def get_movements_chart(self, **params: Any) -> Any:
        return await self._client.get(
            "/inventory/movements/chart", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    # Transfers
    async def list_transfers(self, **params: Any) -> Any:
        return await self._client.get(
            "/inventory/transfers", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create_transfer(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/transfers", json=body)

    async def retrieve_transfer(self, id: str) -> Any:
        return await self._client.get(f"/inventory/transfers/{id}")

    async def update_transfer(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/transfers/{id}", json=body)

    async def delete_transfer(self, id: str) -> Any:
        return await self._client.delete(f"/inventory/transfers/{id}")

    async def complete_transfer(self, id: str) -> Any:
        return await self._client.post(f"/inventory/transfers/{id}/complete")

    # BOMs
    async def list_bom(self, **params: Any) -> Any:
        return await self._client.get(
            "/inventory/bom", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create_bom(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/bom", json=body)

    async def retrieve_bom(self, id: str) -> Any:
        return await self._client.get(f"/inventory/bom/{id}")

    async def update_bom(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/bom/{id}", json=body)

    async def delete_bom(self, id: str) -> Any:
        return await self._client.delete(f"/inventory/bom/{id}")

    async def list_bom_components(self, bom_id: str) -> Any:
        return await self._client.get(f"/inventory/bom/{bom_id}/components")

    async def add_bom_component(self, bom_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/inventory/bom/{bom_id}/components", json=body)

    async def delete_bom_component(self, bom_id: str, component_id: str) -> Any:
        return await self._client.delete(f"/inventory/bom/{bom_id}/components/{component_id}")

    # Assembly orders
    async def list_assembly_orders(self, **params: Any) -> Any:
        return await self._client.get(
            "/inventory/assembly-orders", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create_assembly_order(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/inventory/assembly-orders", json=body)

    async def retrieve_assembly_order(self, id: str) -> Any:
        return await self._client.get(f"/inventory/assembly-orders/{id}")

    async def update_assembly_order(self, id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/inventory/assembly-orders/{id}", json=body)

    async def delete_assembly_order(self, id: str) -> Any:
        return await self._client.delete(f"/inventory/assembly-orders/{id}")

    async def complete_assembly_order(self, id: str) -> Any:
        return await self._client.post(f"/inventory/assembly-orders/{id}/complete")
