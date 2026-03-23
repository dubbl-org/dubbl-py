from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Quotes:
    """Manage quotes."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/quotes", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/quotes", json=body)

    def retrieve(self, quote_id: str) -> Any:
        return self._client.get(f"/quotes/{quote_id}")

    def update(self, quote_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/quotes/{quote_id}", json=body)

    def delete(self, quote_id: str) -> Any:
        return self._client.delete(f"/quotes/{quote_id}")

    def send(self, quote_id: str) -> Any:
        return self._client.post(f"/quotes/{quote_id}/send")

    def accept(self, quote_id: str) -> Any:
        return self._client.post(f"/quotes/{quote_id}/accept")

    def decline(self, quote_id: str) -> Any:
        return self._client.post(f"/quotes/{quote_id}/decline")

    def convert(self, quote_id: str) -> Any:
        return self._client.post(f"/quotes/{quote_id}/convert")


class AsyncQuotes:
    """Manage quotes (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/quotes", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/quotes", json=body)

    async def retrieve(self, quote_id: str) -> Any:
        return await self._client.get(f"/quotes/{quote_id}")

    async def update(self, quote_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/quotes/{quote_id}", json=body)

    async def delete(self, quote_id: str) -> Any:
        return await self._client.delete(f"/quotes/{quote_id}")

    async def send(self, quote_id: str) -> Any:
        return await self._client.post(f"/quotes/{quote_id}/send")

    async def accept(self, quote_id: str) -> Any:
        return await self._client.post(f"/quotes/{quote_id}/accept")

    async def decline(self, quote_id: str) -> Any:
        return await self._client.post(f"/quotes/{quote_id}/decline")

    async def convert(self, quote_id: str) -> Any:
        return await self._client.post(f"/quotes/{quote_id}/convert")
