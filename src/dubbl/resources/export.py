from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class Export:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def all(self, **params: Any) -> Any:
        return self._client.get("/export", params={k: v for k, v in params.items() if v is not None})

    def accounts(self, **params: Any) -> Any:
        return self._client.get("/export/accounts", params={k: v for k, v in params.items() if v is not None})

    def invoices(self, **params: Any) -> Any:
        return self._client.get("/export/invoices", params={k: v for k, v in params.items() if v is not None})

    def bills(self, **params: Any) -> Any:
        return self._client.get("/export/bills", params={k: v for k, v in params.items() if v is not None})

    def entries(self, **params: Any) -> Any:
        return self._client.get("/export/entries", params={k: v for k, v in params.items() if v is not None})

    def contacts(self, **params: Any) -> Any:
        return self._client.get("/export/contacts", params={k: v for k, v in params.items() if v is not None})

    def products(self, **params: Any) -> Any:
        return self._client.get("/export/products", params={k: v for k, v in params.items() if v is not None})

    def bank_transactions(self, **params: Any) -> Any:
        return self._client.get("/export/bank-transactions", params={k: v for k, v in params.items() if v is not None})


class AsyncExport:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def all(self, **params: Any) -> Any:
        return await self._client.get("/export", params={k: v for k, v in params.items() if v is not None})

    async def accounts(self, **params: Any) -> Any:
        return await self._client.get("/export/accounts", params={k: v for k, v in params.items() if v is not None})

    async def invoices(self, **params: Any) -> Any:
        return await self._client.get("/export/invoices", params={k: v for k, v in params.items() if v is not None})

    async def bills(self, **params: Any) -> Any:
        return await self._client.get("/export/bills", params={k: v for k, v in params.items() if v is not None})

    async def entries(self, **params: Any) -> Any:
        return await self._client.get("/export/entries", params={k: v for k, v in params.items() if v is not None})

    async def contacts(self, **params: Any) -> Any:
        return await self._client.get("/export/contacts", params={k: v for k, v in params.items() if v is not None})

    async def products(self, **params: Any) -> Any:
        return await self._client.get("/export/products", params={k: v for k, v in params.items() if v is not None})

    async def bank_transactions(self, **params: Any) -> Any:
        return await self._client.get("/export/bank-transactions", params={k: v for k, v in params.items() if v is not None})
