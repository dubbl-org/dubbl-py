from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class ReminderRules:
    """Manage reminder rules."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/reminder-rules", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/reminder-rules", json=body)

    def retrieve(self, rule_id: str) -> Any:
        return self._client.get(f"/reminder-rules/{rule_id}")

    def update(self, rule_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/reminder-rules/{rule_id}", json=body)

    def delete(self, rule_id: str) -> Any:
        return self._client.delete(f"/reminder-rules/{rule_id}")


class AsyncReminderRules:
    """Manage reminder rules (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/reminder-rules", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/reminder-rules", json=body)

    async def retrieve(self, rule_id: str) -> Any:
        return await self._client.get(f"/reminder-rules/{rule_id}")

    async def update(self, rule_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/reminder-rules/{rule_id}", json=body)

    async def delete(self, rule_id: str) -> Any:
        return await self._client.delete(f"/reminder-rules/{rule_id}")
