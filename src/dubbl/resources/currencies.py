from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class Currencies:
    """Reference currency data."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/currencies", params={k: v for k, v in params.items() if v is not None})


class AsyncCurrencies:
    """Reference currency data (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/currencies", params={k: v for k, v in params.items() if v is not None})
