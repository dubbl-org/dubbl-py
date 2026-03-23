from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class BankImports:
    """Bank imports management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(self, import_id: str) -> ResponseValue:
        return self._client.get(f"/bank-imports/{import_id}")

    def update(self, import_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError("The current v1 API only exposes bank import retrieval; updates are unavailable.")

    def delete(self, import_id: str) -> ResponseValue:
        raise NotImplementedError("The current v1 API only exposes bank import retrieval; deletion is unavailable.")


class AsyncBankImports:
    """Bank imports management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(self, import_id: str) -> ResponseValue:
        return await self._client.get(f"/bank-imports/{import_id}")

    async def update(self, import_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError("The current v1 API only exposes bank import retrieval; updates are unavailable.")

    async def delete(self, import_id: str) -> ResponseValue:
        raise NotImplementedError("The current v1 API only exposes bank import retrieval; deletion is unavailable.")
