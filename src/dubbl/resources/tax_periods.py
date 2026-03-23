from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class TaxPeriods:
    """Manage tax periods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/tax-periods", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/tax-periods", json=body)

    def retrieve(self, period_id: str) -> Any:
        return self._client.get(f"/tax-periods/{period_id}")

    def update(self, period_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/tax-periods/{period_id}", json=body)

    def delete(self, period_id: str) -> Any:
        return self._client.delete(f"/tax-periods/{period_id}")

    def file_return(self, period_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/tax-periods/{period_id}/file", json=body)


class AsyncTaxPeriods:
    """Manage tax periods (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get(
            "/tax-periods", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/tax-periods", json=body)

    async def retrieve(self, period_id: str) -> Any:
        return await self._client.get(f"/tax-periods/{period_id}")

    async def update(self, period_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/tax-periods/{period_id}", json=body)

    async def delete(self, period_id: str) -> Any:
        return await self._client.delete(f"/tax-periods/{period_id}")

    async def file_return(self, period_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/tax-periods/{period_id}/file", json=body)
