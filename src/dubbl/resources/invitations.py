from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Invitations:
    """Manage invitations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/invitations", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/invitations", json=body)

    def retrieve(self, invitation_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes invitation deletion, but not direct retrieval by id."
        )

    def delete(self, invitation_id: str) -> ResponseValue:
        return self._client.delete(f"/invitations/{invitation_id}")

    def get_info(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/invitations/info", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def accept(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/invitations/accept", json=body)


class AsyncInvitations:
    """Manage invitations (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/invitations", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/invitations", json=body)

    async def retrieve(self, invitation_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes invitation deletion, but not direct retrieval by id."
        )

    async def delete(self, invitation_id: str) -> ResponseValue:
        return await self._client.delete(f"/invitations/{invitation_id}")

    async def get_info(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/invitations/info", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def accept(self, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/invitations/accept", json=body)
