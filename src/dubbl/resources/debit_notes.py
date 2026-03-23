from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class DebitNotes:
    """Debit notes management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/debit-notes", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post("/debit-notes", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, debit_note_id: str) -> ResponseValue:
        return self._client.get(f"/debit-notes/{debit_note_id}")

    def update(self, debit_note_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/debit-notes/{debit_note_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete(self, debit_note_id: str) -> ResponseValue:
        return self._client.delete(f"/debit-notes/{debit_note_id}")

    def apply(self, debit_note_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/debit-notes/{debit_note_id}/apply", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def send(self, debit_note_id: str) -> ResponseValue:
        return self._client.post(f"/debit-notes/{debit_note_id}/send")

    def void(self, debit_note_id: str) -> ResponseValue:
        return self._client.post(f"/debit-notes/{debit_note_id}/void")


class AsyncDebitNotes:
    """Debit notes management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/debit-notes", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/debit-notes", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, debit_note_id: str) -> ResponseValue:
        return await self._client.get(f"/debit-notes/{debit_note_id}")

    async def update(self, debit_note_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/debit-notes/{debit_note_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, debit_note_id: str) -> ResponseValue:
        return await self._client.delete(f"/debit-notes/{debit_note_id}")

    async def apply(self, debit_note_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/debit-notes/{debit_note_id}/apply", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def send(self, debit_note_id: str) -> ResponseValue:
        return await self._client.post(f"/debit-notes/{debit_note_id}/send")

    async def void(self, debit_note_id: str) -> ResponseValue:
        return await self._client.post(f"/debit-notes/{debit_note_id}/void")
