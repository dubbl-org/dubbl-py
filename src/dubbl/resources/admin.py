from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Admin:
    """Administrative API surface."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def check(self) -> ResponseValue:
        return self._client.get("/admin/check")

    def email_preview(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/admin/email-preview", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def list_organizations(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/admin/organizations", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def retrieve_organization(self, organization_id: str) -> ResponseValue:
        return self._client.get(f"/admin/organizations/{organization_id}")

    def update_organization(self, organization_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/admin/organizations/{organization_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def cancel_organization_stripe(self, organization_id: str) -> ResponseValue:
        return self._client.post(f"/admin/organizations/{organization_id}/cancel-stripe")

    def get_settings(self) -> ResponseValue:
        return self._client.get("/admin/settings")

    def update_settings(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch("/admin/settings", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def stats(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/admin/stats", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def usage(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/admin/usage", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def list_users(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/admin/users", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def update_user(self, user_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/admin/users/{user_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )


class AsyncAdmin:
    """Administrative API surface (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def check(self) -> ResponseValue:
        return await self._client.get("/admin/check")

    async def email_preview(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/admin/email-preview", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def list_organizations(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/admin/organizations", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def retrieve_organization(self, organization_id: str) -> ResponseValue:
        return await self._client.get(f"/admin/organizations/{organization_id}")

    async def update_organization(self, organization_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/admin/organizations/{organization_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def cancel_organization_stripe(self, organization_id: str) -> ResponseValue:
        return await self._client.post(f"/admin/organizations/{organization_id}/cancel-stripe")

    async def get_settings(self) -> ResponseValue:
        return await self._client.get("/admin/settings")

    async def update_settings(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            "/admin/settings", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def stats(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/admin/stats", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def usage(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/admin/usage", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def list_users(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/admin/users", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def update_user(self, user_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/admin/users/{user_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )
