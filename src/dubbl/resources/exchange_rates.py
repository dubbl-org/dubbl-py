from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class ExchangeRates:
    """Exchange rates management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/exchange-rates", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/exchange-rates", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, rate_id: str) -> Any:
        return self._client.get(f"/exchange-rates/{rate_id}")

    def update(self, rate_id: str, **kwargs: Any) -> Any:
        return self._client.patch(
            f"/exchange-rates/{rate_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete(self, rate_id: str) -> Any:
        return self._client.delete(f"/exchange-rates/{rate_id}")


class AsyncExchangeRates:
    """Exchange rates management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/exchange-rates", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/exchange-rates", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, rate_id: str) -> Any:
        return await self._client.get(f"/exchange-rates/{rate_id}")

    async def update(self, rate_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/exchange-rates/{rate_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, rate_id: str) -> Any:
        return await self._client.delete(f"/exchange-rates/{rate_id}")
