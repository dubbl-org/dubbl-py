from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Attachments:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(self, attachment_id: str) -> Any:
        return self._client.get(f"/attachments/{attachment_id}")

    def delete(self, attachment_id: str) -> Any:
        return self._client.delete(f"/attachments/{attachment_id}")

    def presign(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/attachments/presign", json=body)

    def get_upload_url(self, **kwargs: Any) -> Any:
        return self.presign(**kwargs)


class AsyncAttachments:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(self, attachment_id: str) -> Any:
        return await self._client.get(f"/attachments/{attachment_id}")

    async def delete(self, attachment_id: str) -> Any:
        return await self._client.delete(f"/attachments/{attachment_id}")

    async def presign(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/attachments/presign", json=body)

    async def get_upload_url(self, **kwargs: Any) -> Any:
        return await self.presign(**kwargs)
