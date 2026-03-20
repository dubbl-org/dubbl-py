from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class EmailConfig:
    """Email configuration management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> Any:
        return self._client.get("/email-config")

    def update(self, **kwargs: Any) -> Any:
        return self._client.patch("/email-config", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def test(self, **kwargs: Any) -> Any:
        return self._client.post("/email-config/test", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})


class AsyncEmailConfig:
    """Email configuration management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> Any:
        return await self._client.get("/email-config")

    async def update(self, **kwargs: Any) -> Any:
        return await self._client.patch("/email-config", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def test(self, **kwargs: Any) -> Any:
        return await self._client.post("/email-config/test", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})
