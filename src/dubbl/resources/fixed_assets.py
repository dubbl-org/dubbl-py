from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class FixedAssets:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/fixed-assets", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post("/fixed-assets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> ResponseValue:
        return self._client.get(f"/fixed-assets/{id}")

    def update(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/fixed-assets/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete(self, id: str) -> ResponseValue:
        return self._client.delete(f"/fixed-assets/{id}")

    def depreciate(self, id: str) -> ResponseValue:
        return self._client.post(f"/fixed-assets/{id}/depreciate")

    def dispose(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/fixed-assets/{id}/dispose", json=body)

    def run_depreciation(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/fixed-assets/run-depreciation", json=body)


class AsyncFixedAssets:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/fixed-assets", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/fixed-assets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, id: str) -> ResponseValue:
        return await self._client.get(f"/fixed-assets/{id}")

    async def update(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/fixed-assets/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, id: str) -> ResponseValue:
        return await self._client.delete(f"/fixed-assets/{id}")

    async def depreciate(self, id: str) -> ResponseValue:
        return await self._client.post(f"/fixed-assets/{id}/depreciate")

    async def dispose(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/fixed-assets/{id}/dispose", json=body)

    async def run_depreciation(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/fixed-assets/run-depreciation", json=body)
