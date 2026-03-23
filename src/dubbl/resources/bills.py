from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Bills:
    """Manage bills."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/bills", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/bills", json=body)

    def retrieve(self, bill_id: str) -> ResponseValue:
        return self._client.get(f"/bills/{bill_id}")

    def update(self, bill_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/bills/{bill_id}", json=body)

    def delete(self, bill_id: str) -> ResponseValue:
        return self._client.delete(f"/bills/{bill_id}")

    def approve(self, bill_id: str) -> ResponseValue:
        return self._client.post(f"/bills/{bill_id}/approve")

    def reject(self, bill_id: str) -> ResponseValue:
        return self._client.post(f"/bills/{bill_id}/reject")

    def receive(self, bill_id: str) -> ResponseValue:
        return self._client.post(f"/bills/{bill_id}/receive")

    def pay(self, bill_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bills/{bill_id}/pay", json=body)

    def void(self, bill_id: str) -> ResponseValue:
        return self._client.post(f"/bills/{bill_id}/void")

    def counts(self) -> ResponseValue:
        return self._client.get("/bills/counts")


class AsyncBills:
    """Manage bills (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/bills", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/bills", json=body)

    async def retrieve(self, bill_id: str) -> ResponseValue:
        return await self._client.get(f"/bills/{bill_id}")

    async def update(self, bill_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/bills/{bill_id}", json=body)

    async def delete(self, bill_id: str) -> ResponseValue:
        return await self._client.delete(f"/bills/{bill_id}")

    async def approve(self, bill_id: str) -> ResponseValue:
        return await self._client.post(f"/bills/{bill_id}/approve")

    async def reject(self, bill_id: str) -> ResponseValue:
        return await self._client.post(f"/bills/{bill_id}/reject")

    async def receive(self, bill_id: str) -> ResponseValue:
        return await self._client.post(f"/bills/{bill_id}/receive")

    async def pay(self, bill_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bills/{bill_id}/pay", json=body)

    async def void(self, bill_id: str) -> ResponseValue:
        return await self._client.post(f"/bills/{bill_id}/void")

    async def counts(self) -> ResponseValue:
        return await self._client.get("/bills/counts")
