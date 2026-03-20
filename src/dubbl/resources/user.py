from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


class User:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> Any:
        return self._client.get("/user")


class AsyncUser:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> Any:
        return await self._client.get("/user")
