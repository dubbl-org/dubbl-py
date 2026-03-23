from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class PurchaseRequisitions:
    """Manage purchase requisitions."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/purchase-requisitions", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/purchase-requisitions", json=body)

    def retrieve(self, requisition_id: str) -> ResponseValue:
        return self._client.get(f"/purchase-requisitions/{requisition_id}")

    def update(self, requisition_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.put(f"/purchase-requisitions/{requisition_id}", json=body)

    def delete(self, requisition_id: str) -> ResponseValue:
        return self._client.delete(f"/purchase-requisitions/{requisition_id}")

    def approve(self, requisition_id: str) -> ResponseValue:
        return self._client.post(f"/purchase-requisitions/{requisition_id}/approve")

    def reject(self, requisition_id: str) -> ResponseValue:
        return self._client.post(f"/purchase-requisitions/{requisition_id}/reject")

    def convert(self, requisition_id: str) -> ResponseValue:
        return self._client.post(f"/purchase-requisitions/{requisition_id}/convert")


class AsyncPurchaseRequisitions:
    """Manage purchase requisitions (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/purchase-requisitions", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/purchase-requisitions", json=body)

    async def retrieve(self, requisition_id: str) -> ResponseValue:
        return await self._client.get(f"/purchase-requisitions/{requisition_id}")

    async def update(self, requisition_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.put(f"/purchase-requisitions/{requisition_id}", json=body)

    async def delete(self, requisition_id: str) -> ResponseValue:
        return await self._client.delete(f"/purchase-requisitions/{requisition_id}")

    async def approve(self, requisition_id: str) -> ResponseValue:
        return await self._client.post(f"/purchase-requisitions/{requisition_id}/approve")

    async def reject(self, requisition_id: str) -> ResponseValue:
        return await self._client.post(f"/purchase-requisitions/{requisition_id}/reject")

    async def convert(self, requisition_id: str) -> ResponseValue:
        return await self._client.post(f"/purchase-requisitions/{requisition_id}/convert")
