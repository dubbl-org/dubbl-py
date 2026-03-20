from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Attachments:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get_upload_url(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/attachments/upload-url", json=body)


class AsyncAttachments:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get_upload_url(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/attachments/upload-url", json=body)
