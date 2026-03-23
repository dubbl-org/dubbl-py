from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class ApprovalRequests:
    """Approval requests management."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/approval-requests", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/approval-requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve(self, request_id: str) -> ResponseValue:
        return self._client.get(f"/approval-requests/{request_id}")

    def update(self, request_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes approval request retrieval and actions, but not direct updates."
        )

    def delete(self, request_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes approval request retrieval and actions, but not direct deletion."
        )

    def action(self, request_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/approval-requests/{request_id}/action",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )


class AsyncApprovalRequests:
    """Approval requests management."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/approval-requests", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/approval-requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve(self, request_id: str) -> ResponseValue:
        return await self._client.get(f"/approval-requests/{request_id}")

    async def update(self, request_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes approval request retrieval and actions, but not direct updates."
        )

    async def delete(self, request_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes approval request retrieval and actions, but not direct deletion."
        )

    async def action(self, request_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/approval-requests/{request_id}/action",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )
