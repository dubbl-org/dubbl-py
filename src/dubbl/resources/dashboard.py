from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Dashboard:
    """Dashboard management - alerts, layouts, widgets."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get_alerts(self) -> ResponseValue:
        return self._client.get("/dashboard/alerts")

    def list_layouts(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/dashboard/layouts", params={k: v for k, v in params.items() if v is not None})

    def create_layout(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/dashboard/layouts", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_layout(self, layout_id: str) -> ResponseValue:
        return self._client.get(f"/dashboard/layouts/{layout_id}")

    def update_layout(self, layout_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/dashboard/layouts/{layout_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_layout(self, layout_id: str) -> ResponseValue:
        return self._client.delete(f"/dashboard/layouts/{layout_id}")

    def get_widget_data(self, widget_type: str, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            f"/dashboard/widgets/{widget_type}/data", params={k: v for k, v in params.items() if v is not None}
        )


class AsyncDashboard:
    """Dashboard management - alerts, layouts, widgets."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get_alerts(self) -> ResponseValue:
        return await self._client.get("/dashboard/alerts")

    async def list_layouts(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/dashboard/layouts", params={k: v for k, v in params.items() if v is not None})

    async def create_layout(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/dashboard/layouts", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_layout(self, layout_id: str) -> ResponseValue:
        return await self._client.get(f"/dashboard/layouts/{layout_id}")

    async def update_layout(self, layout_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/dashboard/layouts/{layout_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_layout(self, layout_id: str) -> ResponseValue:
        return await self._client.delete(f"/dashboard/layouts/{layout_id}")

    async def get_widget_data(self, widget_type: str, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            f"/dashboard/widgets/{widget_type}/data", params={k: v for k, v in params.items() if v is not None}
        )
