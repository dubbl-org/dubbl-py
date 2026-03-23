from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class OpeningBalances:
    """Manage opening balances."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        raise NotImplementedError(
            "The current API only supports creating opening balances; listing historical opening balances is"
            " unavailable."
        )

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/opening-balances", json=body)

    def retrieve(self, balance_id: str) -> ResponseValue:
        raise NotImplementedError("The current API does not expose opening balance retrieval by id.")

    def update(self, balance_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current API replaces opening balances via create(); update-by-id is unavailable."
        )

    def delete(self, balance_id: str) -> ResponseValue:
        raise NotImplementedError("The current API does not support deleting opening balances by id.")


class AsyncOpeningBalances:
    """Manage opening balances (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        raise NotImplementedError(
            "The current API only supports creating opening balances; listing historical opening balances is"
            " unavailable."
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/opening-balances", json=body)

    async def retrieve(self, balance_id: str) -> ResponseValue:
        raise NotImplementedError("The current API does not expose opening balance retrieval by id.")

    async def update(self, balance_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current API replaces opening balances via create(); update-by-id is unavailable."
        )

    async def delete(self, balance_id: str) -> ResponseValue:
        raise NotImplementedError("The current API does not support deleting opening balances by id.")
