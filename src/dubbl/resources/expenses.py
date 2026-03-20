from __future__ import annotations
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Expenses:
    """Manage expenses."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/expenses", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(
        self,
        *,
        title: str,
        description: Optional[str] = None,
        currency_code: Optional[str] = None,
        items: Optional[List[Dict[str, Any]]] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "title": title,
            "description": description,
            "currencyCode": currency_code,
            "items": items,
        }
        return self._client.post("/expenses", json={k: v for k, v in body.items() if v is not None})

    def retrieve(self, expense_id: str) -> Any:
        return self._client.get(f"/expenses/{expense_id}")

    def update(self, expense_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/expenses/{expense_id}", json=body)

    def delete(self, expense_id: str) -> Any:
        return self._client.delete(f"/expenses/{expense_id}")

    def submit(self, expense_id: str) -> Any:
        return self._client.post(f"/expenses/{expense_id}/submit")

    def approve(self, expense_id: str) -> Any:
        return self._client.post(f"/expenses/{expense_id}/approve")

    def reject(self, expense_id: str) -> Any:
        return self._client.post(f"/expenses/{expense_id}/reject")

    def pay(self, expense_id: str) -> Any:
        return self._client.post(f"/expenses/{expense_id}/pay")


class AsyncExpenses:
    """Manage expenses (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/expenses", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(
        self,
        *,
        title: str,
        description: Optional[str] = None,
        currency_code: Optional[str] = None,
        items: Optional[List[Dict[str, Any]]] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "title": title,
            "description": description,
            "currencyCode": currency_code,
            "items": items,
        }
        return await self._client.post("/expenses", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, expense_id: str) -> Any:
        return await self._client.get(f"/expenses/{expense_id}")

    async def update(self, expense_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/expenses/{expense_id}", json=body)

    async def delete(self, expense_id: str) -> Any:
        return await self._client.delete(f"/expenses/{expense_id}")

    async def submit(self, expense_id: str) -> Any:
        return await self._client.post(f"/expenses/{expense_id}/submit")

    async def approve(self, expense_id: str) -> Any:
        return await self._client.post(f"/expenses/{expense_id}/approve")

    async def reject(self, expense_id: str) -> Any:
        return await self._client.post(f"/expenses/{expense_id}/reject")

    async def pay(self, expense_id: str) -> Any:
        return await self._client.post(f"/expenses/{expense_id}/pay")
