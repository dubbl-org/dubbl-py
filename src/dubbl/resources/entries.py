from __future__ import annotations
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Entries:
    """Manage journal entries."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/entries", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(
        self,
        *,
        date: str,
        description: str,
        lines: List[Dict[str, Any]],
        reference: Optional[str] = None,
        fiscal_year_id: Optional[str] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "date": date,
            "description": description,
            "lines": lines,
            "reference": reference,
            "fiscalYearId": fiscal_year_id,
        }
        return self._client.post("/entries", json={k: v for k, v in body.items() if v is not None})

    def retrieve(self, entry_id: str) -> Any:
        return self._client.get(f"/entries/{entry_id}")

    def delete(self, entry_id: str) -> Any:
        return self._client.delete(f"/entries/{entry_id}")

    def post(self, entry_id: str) -> Any:
        return self._client.post(f"/entries/{entry_id}/post")

    def void(self, entry_id: str, *, reason: str) -> Any:
        return self._client.post(f"/entries/{entry_id}/void", json={"reason": reason})


class AsyncEntries:
    """Manage journal entries (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/entries", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(
        self,
        *,
        date: str,
        description: str,
        lines: List[Dict[str, Any]],
        reference: Optional[str] = None,
        fiscal_year_id: Optional[str] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "date": date,
            "description": description,
            "lines": lines,
            "reference": reference,
            "fiscalYearId": fiscal_year_id,
        }
        return await self._client.post("/entries", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, entry_id: str) -> Any:
        return await self._client.get(f"/entries/{entry_id}")

    async def delete(self, entry_id: str) -> Any:
        return await self._client.delete(f"/entries/{entry_id}")

    async def post(self, entry_id: str) -> Any:
        return await self._client.post(f"/entries/{entry_id}/post")

    async def void(self, entry_id: str, *, reason: str) -> Any:
        return await self._client.post(f"/entries/{entry_id}/void", json={"reason": reason})
