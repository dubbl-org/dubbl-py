from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class StockTakes:
    """Manage stock takes."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/stock-takes", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/stock-takes", json=body)

    def retrieve(self, stock_take_id: str) -> Any:
        return self._client.get(f"/stock-takes/{stock_take_id}")

    def update(self, stock_take_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/stock-takes/{stock_take_id}", json=body)

    def delete(self, stock_take_id: str) -> Any:
        return self._client.delete(f"/stock-takes/{stock_take_id}")

    def apply(self, stock_take_id: str) -> Any:
        return self._client.post(f"/stock-takes/{stock_take_id}/apply")

    def get_line(self, stock_take_id: str, line_id: str) -> Any:
        return self._client.get(f"/stock-takes/{stock_take_id}/lines/{line_id}")

    def update_line(self, stock_take_id: str, line_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/stock-takes/{stock_take_id}/lines/{line_id}", json=body)

    def delete_line(self, stock_take_id: str, line_id: str) -> Any:
        return self._client.delete(f"/stock-takes/{stock_take_id}/lines/{line_id}")


class AsyncStockTakes:
    """Manage stock takes (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get(
            "/stock-takes", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/stock-takes", json=body)

    async def retrieve(self, stock_take_id: str) -> Any:
        return await self._client.get(f"/stock-takes/{stock_take_id}")

    async def update(self, stock_take_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/stock-takes/{stock_take_id}", json=body)

    async def delete(self, stock_take_id: str) -> Any:
        return await self._client.delete(f"/stock-takes/{stock_take_id}")

    async def apply(self, stock_take_id: str) -> Any:
        return await self._client.post(f"/stock-takes/{stock_take_id}/apply")

    async def get_line(self, stock_take_id: str, line_id: str) -> Any:
        return await self._client.get(f"/stock-takes/{stock_take_id}/lines/{line_id}")

    async def update_line(self, stock_take_id: str, line_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/stock-takes/{stock_take_id}/lines/{line_id}", json=body)

    async def delete_line(self, stock_take_id: str, line_id: str) -> Any:
        return await self._client.delete(f"/stock-takes/{stock_take_id}/lines/{line_id}")
