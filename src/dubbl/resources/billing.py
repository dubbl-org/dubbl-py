from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Billing:
    """Manage billing."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> Any:
        return self._client.get("/billing")

    def create_checkout(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/billing/checkout", json=body)

    def create_portal(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/billing/portal", json=body)


class AsyncBilling:
    """Manage billing (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> Any:
        return await self._client.get("/billing")

    async def create_checkout(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/billing/checkout", json=body)

    async def create_portal(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/billing/portal", json=body)
