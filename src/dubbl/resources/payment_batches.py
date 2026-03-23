from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class PaymentBatches:
    """Manage payment batches."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payment-batches", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/payment-batches", json=body)

    def retrieve(self, batch_id: str) -> ResponseValue:
        return self._client.get(f"/payment-batches/{batch_id}")

    def update(self, batch_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/payment-batches/{batch_id}", json=body)

    def delete(self, batch_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes payment batch retrieval and updates, but not direct deletion."
        )

    def submit(self, batch_id: str) -> ResponseValue:
        return self._client.post(f"/payment-batches/{batch_id}/submit")


class AsyncPaymentBatches:
    """Manage payment batches (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payment-batches", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/payment-batches", json=body)

    async def retrieve(self, batch_id: str) -> ResponseValue:
        return await self._client.get(f"/payment-batches/{batch_id}")

    async def update(self, batch_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/payment-batches/{batch_id}", json=body)

    async def delete(self, batch_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes payment batch retrieval and updates, but not direct deletion."
        )

    async def submit(self, batch_id: str) -> ResponseValue:
        return await self._client.post(f"/payment-batches/{batch_id}/submit")
