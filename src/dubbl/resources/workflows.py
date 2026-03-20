from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Workflows:
    """Manage workflows (automation)."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/workflows", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/workflows", json=body)

    def retrieve(self, workflow_id: str) -> Any:
        return self._client.get(f"/workflows/{workflow_id}")

    def update(self, workflow_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/workflows/{workflow_id}", json=body)

    def delete(self, workflow_id: str) -> Any:
        return self._client.delete(f"/workflows/{workflow_id}")

    def toggle(self, workflow_id: str) -> Any:
        return self._client.post(f"/workflows/{workflow_id}/toggle")

    def test(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/workflows/test", json=body)

    def get_logs(self, workflow_id: str) -> Any:
        return self._client.get(f"/workflows/{workflow_id}/logs")


class AsyncWorkflows:
    """Manage workflows (automation) (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/workflows", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/workflows", json=body)

    async def retrieve(self, workflow_id: str) -> Any:
        return await self._client.get(f"/workflows/{workflow_id}")

    async def update(self, workflow_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/workflows/{workflow_id}", json=body)

    async def delete(self, workflow_id: str) -> Any:
        return await self._client.delete(f"/workflows/{workflow_id}")

    async def toggle(self, workflow_id: str) -> Any:
        return await self._client.post(f"/workflows/{workflow_id}/toggle")

    async def test(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/workflows/test", json=body)

    async def get_logs(self, workflow_id: str) -> Any:
        return await self._client.get(f"/workflows/{workflow_id}/logs")
