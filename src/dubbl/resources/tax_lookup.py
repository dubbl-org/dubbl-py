from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class TaxLookup:
    """Tax lookup."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def lookup(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/tax-lookup", params={_to_camel(k): v for k, v in params.items() if v is not None})


class AsyncTaxLookup:
    """Tax lookup (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def lookup(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/tax-lookup", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )
