from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Accounts:
    """Manage chart of accounts."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        search: str | None = None,
        type: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> ResponseValue:
        params: dict[str, JSONValue] = {"search": search, "type": type, "page": page, "limit": limit}
        return self._client.get("/accounts", params=params)

    def create(
        self,
        *,
        code: str,
        name: str,
        type: str,
        sub_type: str | None = None,
        parent_id: str | None = None,
        currency_code: str | None = None,
        description: str | None = None,
    ) -> ResponseValue:
        body: dict[str, JSONValue] = {
            "code": code,
            "name": name,
            "type": type,
            "subType": sub_type,
            "parentId": parent_id,
            "currencyCode": currency_code,
            "description": description,
        }
        return self._client.post("/accounts", json={k: v for k, v in body.items() if v is not None})

    def retrieve(
        self,
        account_id: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        search: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        entry_type: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
    ) -> ResponseValue:
        params: dict[str, JSONValue] = {
            "page": page,
            "limit": limit,
            "search": search,
            "from": from_date,
            "to": to_date,
            "entryType": entry_type,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
        return self._client.get(f"/accounts/{account_id}", params=params)

    def update(self, account_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/accounts/{account_id}", json=body)

    def delete(self, account_id: str) -> ResponseValue:
        return self._client.delete(f"/accounts/{account_id}")


class AsyncAccounts:
    """Manage chart of accounts (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        search: str | None = None,
        type: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> ResponseValue:
        params: dict[str, JSONValue] = {"search": search, "type": type, "page": page, "limit": limit}
        return await self._client.get("/accounts", params=params)

    async def create(
        self,
        *,
        code: str,
        name: str,
        type: str,
        sub_type: str | None = None,
        parent_id: str | None = None,
        currency_code: str | None = None,
        description: str | None = None,
    ) -> ResponseValue:
        body: dict[str, JSONValue] = {
            "code": code,
            "name": name,
            "type": type,
            "subType": sub_type,
            "parentId": parent_id,
            "currencyCode": currency_code,
            "description": description,
        }
        return await self._client.post("/accounts", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, account_id: str, **kwargs: JSONValue) -> ResponseValue:
        params = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.get(f"/accounts/{account_id}", params=params)

    async def update(self, account_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/accounts/{account_id}", json=body)

    async def delete(self, account_id: str) -> ResponseValue:
        return await self._client.delete(f"/accounts/{account_id}")
