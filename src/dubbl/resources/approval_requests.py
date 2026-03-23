from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class ApprovalRequests:
    """Approval requests management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/approval-requests", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/approval-requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve(self, request_id: str) -> Any:
        return self._client.get(f"/approval-requests/{request_id}")

    def update(self, request_id: str, **kwargs: Any) -> Any:
        return self._client.patch(
            f"/approval-requests/{request_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete(self, request_id: str) -> Any:
        return self._client.delete(f"/approval-requests/{request_id}")

    def action(self, request_id: str, **kwargs: Any) -> Any:
        return self._client.post(
            f"/approval-requests/{request_id}/action",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )


class AsyncApprovalRequests:
    """Approval requests management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/approval-requests", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/approval-requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, request_id: str) -> Any:
        return await self._client.get(f"/approval-requests/{request_id}")

    async def update(self, request_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/approval-requests/{request_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, request_id: str) -> Any:
        return await self._client.delete(f"/approval-requests/{request_id}")

    async def action(self, request_id: str, **kwargs: Any) -> Any:
        return await self._client.post(
            f"/approval-requests/{request_id}/action",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )
