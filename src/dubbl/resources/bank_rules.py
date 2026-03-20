from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class BankRules:
    """Bank rules management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/bank-rules", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/bank-rules", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, rule_id: str) -> Any:
        return self._client.get(f"/bank-rules/{rule_id}")

    def update(self, rule_id: str, **kwargs: Any) -> Any:
        return self._client.patch(f"/bank-rules/{rule_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, rule_id: str) -> Any:
        return self._client.delete(f"/bank-rules/{rule_id}")

    def get_suggestions(self, **params: Any) -> Any:
        return self._client.get("/bank-rules/suggestions", params={k: v for k, v in params.items() if v is not None})


class AsyncBankRules:
    """Bank rules management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/bank-rules", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post("/bank-rules", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, rule_id: str) -> Any:
        return await self._client.get(f"/bank-rules/{rule_id}")

    async def update(self, rule_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(f"/bank-rules/{rule_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def delete(self, rule_id: str) -> Any:
        return await self._client.delete(f"/bank-rules/{rule_id}")

    async def get_suggestions(self, **params: Any) -> Any:
        return await self._client.get("/bank-rules/suggestions", params={k: v for k, v in params.items() if v is not None})
