from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class BankImports:
    """Bank imports management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(self, import_id: str) -> Any:
        return self._client.get(f"/bank-imports/{import_id}")

    def update(self, import_id: str, **kwargs: Any) -> Any:
        return self._client.patch(
            f"/bank-imports/{import_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete(self, import_id: str) -> Any:
        return self._client.delete(f"/bank-imports/{import_id}")


class AsyncBankImports:
    """Bank imports management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(self, import_id: str) -> Any:
        return await self._client.get(f"/bank-imports/{import_id}")

    async def update(self, import_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/bank-imports/{import_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, import_id: str) -> Any:
        return await self._client.delete(f"/bank-imports/{import_id}")
