from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class LandedCosts:
    """Manage landed costs."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/landed-costs", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/landed-costs", json=body)

    def retrieve(self, cost_id: str) -> Any:
        return self._client.get(f"/landed-costs/{cost_id}")

    def update(self, cost_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/landed-costs/{cost_id}", json=body)

    def delete(self, cost_id: str) -> Any:
        return self._client.delete(f"/landed-costs/{cost_id}")

    def allocate(self, cost_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/landed-costs/{cost_id}/allocate", json=body)


class AsyncLandedCosts:
    """Manage landed costs (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/landed-costs", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/landed-costs", json=body)

    async def retrieve(self, cost_id: str) -> Any:
        return await self._client.get(f"/landed-costs/{cost_id}")

    async def update(self, cost_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/landed-costs/{cost_id}", json=body)

    async def delete(self, cost_id: str) -> Any:
        return await self._client.delete(f"/landed-costs/{cost_id}")

    async def allocate(self, cost_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/landed-costs/{cost_id}/allocate", json=body)
