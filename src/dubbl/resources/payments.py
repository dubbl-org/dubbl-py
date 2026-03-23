from __future__ import annotations

import builtins
from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Payments:
    """Manage payments."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payments", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(
        self,
        *,
        contact_id: str,
        type: str,
        date: str,
        amount: JSONValue,
        method: str | None = None,
        reference: str | None = None,
        notes: str | None = None,
        bank_account_id: str | None = None,
        allocations: builtins.list[dict[str, JSONValue]] | None = None,
    ) -> ResponseValue:
        body: dict[str, JSONValue] = {
            "contactId": contact_id,
            "type": type,
            "date": date,
            "amount": amount,
            "method": method,
            "reference": reference,
            "notes": notes,
            "bankAccountId": bank_account_id,
            "allocations": allocations,
        }
        return self._client.post("/payments", json={k: v for k, v in body.items() if v is not None})

    def retrieve(self, payment_id: str) -> ResponseValue:
        return self._client.get(f"/payments/{payment_id}")

    def update(self, payment_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError("The current v1 API exposes payment retrieval and deletion, but not direct updates.")

    def delete(self, payment_id: str) -> ResponseValue:
        return self._client.delete(f"/payments/{payment_id}")

    def batch(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/payments/batch", json=body)


class AsyncPayments:
    """Manage payments (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payments", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(
        self,
        *,
        contact_id: str,
        type: str,
        date: str,
        amount: JSONValue,
        method: str | None = None,
        reference: str | None = None,
        notes: str | None = None,
        bank_account_id: str | None = None,
        allocations: builtins.list[dict[str, JSONValue]] | None = None,
    ) -> ResponseValue:
        body: dict[str, JSONValue] = {
            "contactId": contact_id,
            "type": type,
            "date": date,
            "amount": amount,
            "method": method,
            "reference": reference,
            "notes": notes,
            "bankAccountId": bank_account_id,
            "allocations": allocations,
        }
        return await self._client.post("/payments", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, payment_id: str) -> ResponseValue:
        return await self._client.get(f"/payments/{payment_id}")

    async def update(self, payment_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError("The current v1 API exposes payment retrieval and deletion, but not direct updates.")

    async def delete(self, payment_id: str) -> ResponseValue:
        return await self._client.delete(f"/payments/{payment_id}")

    async def batch(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/payments/batch", json=body)
