from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Portal:
    """Manage portal access and public portal endpoints."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    # --- Access management ---

    def list_access(self, **params: Any) -> Any:
        return self._client.get("/portal", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create_access(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/portal", json=body)

    def retrieve_access(self, access_id: str) -> Any:
        return self._client.get(f"/portal/{access_id}")

    def update_access(self, access_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/portal/{access_id}", json=body)

    def delete_access(self, access_id: str) -> Any:
        return self._client.delete(f"/portal/{access_id}")

    def invite(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/portal/invite", json=body)

    # --- Public portal endpoints ---

    def get_statements(self, token: str, **params: Any) -> Any:
        return self._client.get(f"/portal/{token}/statements", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def list_payments(self, token: str) -> Any:
        return self._client.get(f"/portal/{token}/payments")

    def make_payment(self, token: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/portal/{token}/payments", json=body)

    def list_quotes(self, token: str) -> Any:
        return self._client.get(f"/portal/{token}/quotes")

    def accept_quote(self, token: str, quote_id: str) -> Any:
        return self._client.post(f"/portal/{token}/quotes/{quote_id}/accept")


class AsyncPortal:
    """Manage portal access and public portal endpoints (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    # --- Access management ---

    async def list_access(self, **params: Any) -> Any:
        return await self._client.get("/portal", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create_access(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/portal", json=body)

    async def retrieve_access(self, access_id: str) -> Any:
        return await self._client.get(f"/portal/{access_id}")

    async def update_access(self, access_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/portal/{access_id}", json=body)

    async def delete_access(self, access_id: str) -> Any:
        return await self._client.delete(f"/portal/{access_id}")

    async def invite(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/portal/invite", json=body)

    # --- Public portal endpoints ---

    async def get_statements(self, token: str, **params: Any) -> Any:
        return await self._client.get(f"/portal/{token}/statements", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def list_payments(self, token: str) -> Any:
        return await self._client.get(f"/portal/{token}/payments")

    async def make_payment(self, token: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/portal/{token}/payments", json=body)

    async def list_quotes(self, token: str) -> Any:
        return await self._client.get(f"/portal/{token}/quotes")

    async def accept_quote(self, token: str, quote_id: str) -> Any:
        return await self._client.post(f"/portal/{token}/quotes/{quote_id}/accept")
