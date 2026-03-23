from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Integrations:
    """Third-party integration endpoints."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def connect_stripe(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/integrations/stripe/connect", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def handle_stripe_callback(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/integrations/stripe/callback", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def get_stripe_status(self) -> ResponseValue:
        return self._client.get("/integrations/stripe/status")

    def update_stripe_settings(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            "/integrations/stripe/settings", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def sync_stripe(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/integrations/stripe/sync", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def import_stripe_data(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/integrations/stripe/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def reconcile_stripe(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/integrations/stripe/reconcile", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def disconnect_stripe(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/integrations/stripe/disconnect", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )


class AsyncIntegrations:
    """Third-party integration endpoints (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def connect_stripe(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/integrations/stripe/connect", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def handle_stripe_callback(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/integrations/stripe/callback", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def get_stripe_status(self) -> ResponseValue:
        return await self._client.get("/integrations/stripe/status")

    async def update_stripe_settings(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            "/integrations/stripe/settings", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def sync_stripe(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/integrations/stripe/sync", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def import_stripe_data(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/integrations/stripe/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def reconcile_stripe(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/integrations/stripe/reconcile", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def disconnect_stripe(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/integrations/stripe/disconnect", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )
