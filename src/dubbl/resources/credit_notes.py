from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class CreditNotes:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/credit-notes", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post("/credit-notes", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> ResponseValue:
        return self._client.get(f"/credit-notes/{id}")

    def update(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/credit-notes/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete(self, id: str) -> ResponseValue:
        return self._client.delete(f"/credit-notes/{id}")

    def summary(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/credit-notes/summary", params={k: v for k, v in params.items() if v is not None})

    def apply(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/credit-notes/{id}/apply", json=body)

    def send(self, id: str) -> ResponseValue:
        return self._client.post(f"/credit-notes/{id}/send")

    def void(self, id: str) -> ResponseValue:
        return self._client.post(f"/credit-notes/{id}/void")


class AsyncCreditNotes:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/credit-notes", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/credit-notes", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, id: str) -> ResponseValue:
        return await self._client.get(f"/credit-notes/{id}")

    async def update(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/credit-notes/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, id: str) -> ResponseValue:
        return await self._client.delete(f"/credit-notes/{id}")

    async def summary(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/credit-notes/summary", params={k: v for k, v in params.items() if v is not None}
        )

    async def apply(self, id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/credit-notes/{id}/apply", json=body)

    async def send(self, id: str) -> ResponseValue:
        return await self._client.post(f"/credit-notes/{id}/send")

    async def void(self, id: str) -> ResponseValue:
        return await self._client.post(f"/credit-notes/{id}/void")
