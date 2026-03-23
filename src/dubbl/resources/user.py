from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class User:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> ResponseValue:
        return self._client.get("/user/profile")

    def update_profile(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch("/user/profile", json=body)

    def list_accounts(self) -> ResponseValue:
        return self._client.get("/user/accounts")

    def delete_account(self, account_id: str) -> ResponseValue:
        return self._client.delete(f"/user/accounts/{account_id}")


class AsyncUser:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> ResponseValue:
        return await self._client.get("/user/profile")

    async def update_profile(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch("/user/profile", json=body)

    async def list_accounts(self) -> ResponseValue:
        return await self._client.get("/user/accounts")

    async def delete_account(self, account_id: str) -> ResponseValue:
        return await self._client.delete(f"/user/accounts/{account_id}")
