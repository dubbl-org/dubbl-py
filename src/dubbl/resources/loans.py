from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Loans:
    """Manage loans."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/loans", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/loans", json=body)

    def retrieve(self, loan_id: str) -> Any:
        return self._client.get(f"/loans/{loan_id}")

    def update(self, loan_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/loans/{loan_id}", json=body)

    def delete(self, loan_id: str) -> Any:
        return self._client.delete(f"/loans/{loan_id}")

    def post_payment(self, loan_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/loans/{loan_id}/post-payment", json=body)


class AsyncLoans:
    """Manage loans (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/loans", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/loans", json=body)

    async def retrieve(self, loan_id: str) -> Any:
        return await self._client.get(f"/loans/{loan_id}")

    async def update(self, loan_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/loans/{loan_id}", json=body)

    async def delete(self, loan_id: str) -> Any:
        return await self._client.delete(f"/loans/{loan_id}")

    async def post_payment(self, loan_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/loans/{loan_id}/post-payment", json=body)
