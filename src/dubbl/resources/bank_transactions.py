from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class BankTransactions:
    """Manage bank transactions."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def reconcile(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-transactions/{transaction_id}/reconcile", json=body)

    def unreconcile(self, transaction_id: str) -> Any:
        return self._client.post(f"/bank-transactions/{transaction_id}/unreconcile")

    def match(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-transactions/{transaction_id}/match", json=body)

    def match_invoice(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-transactions/{transaction_id}/match-invoice", json=body)

    def split(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-transactions/{transaction_id}/split", json=body)

    def exclude(self, transaction_id: str) -> Any:
        return self._client.post(f"/bank-transactions/{transaction_id}/exclude")

    def suggestions(self, transaction_id: str) -> Any:
        return self._client.get(f"/bank-transactions/{transaction_id}/suggestions")

    def create_expense(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-transactions/{transaction_id}/expense", json=body)

    def activity(self, transaction_id: str) -> Any:
        return self._client.get(f"/bank-transactions/{transaction_id}/activity")


class AsyncBankTransactions:
    """Manage bank transactions (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def reconcile(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-transactions/{transaction_id}/reconcile", json=body)

    async def unreconcile(self, transaction_id: str) -> Any:
        return await self._client.post(f"/bank-transactions/{transaction_id}/unreconcile")

    async def match(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-transactions/{transaction_id}/match", json=body)

    async def match_invoice(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-transactions/{transaction_id}/match-invoice", json=body)

    async def split(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-transactions/{transaction_id}/split", json=body)

    async def exclude(self, transaction_id: str) -> Any:
        return await self._client.post(f"/bank-transactions/{transaction_id}/exclude")

    async def suggestions(self, transaction_id: str) -> Any:
        return await self._client.get(f"/bank-transactions/{transaction_id}/suggestions")

    async def create_expense(self, transaction_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-transactions/{transaction_id}/expense", json=body)

    async def activity(self, transaction_id: str) -> Any:
        return await self._client.get(f"/bank-transactions/{transaction_id}/activity")
