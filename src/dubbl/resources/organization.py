from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Organization:
    """Manage organization."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def get(self) -> Any:
        return self._client.get("/organization")

    def create(self, *, name: str, slug: str) -> Any:
        return self._client.post("/organization", json={"name": name, "slug": slug})

    def update(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch("/organization", json=body)

    def invite_link(self, org_id: str) -> Any:
        return self._client.get(f"/organization/{org_id}/invite-link")

    def get_settings(self, org_id: str) -> Any:
        return self._client.get(f"/organization/{org_id}/settings")

    def update_settings(self, org_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/organization/{org_id}/settings", json=body)

    def get_mileage_rate(self) -> Any:
        return self._client.get("/organization/mileage-rate")

    def update_mileage_rate(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch("/organization/mileage-rate", json=body)


class AsyncOrganization:
    """Manage organization (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def get(self) -> Any:
        return await self._client.get("/organization")

    async def create(self, *, name: str, slug: str) -> Any:
        return await self._client.post("/organization", json={"name": name, "slug": slug})

    async def update(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch("/organization", json=body)

    async def invite_link(self, org_id: str) -> Any:
        return await self._client.get(f"/organization/{org_id}/invite-link")

    async def get_settings(self, org_id: str) -> Any:
        return await self._client.get(f"/organization/{org_id}/settings")

    async def update_settings(self, org_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/organization/{org_id}/settings", json=body)

    async def get_mileage_rate(self) -> Any:
        return await self._client.get("/organization/mileage-rate")

    async def update_mileage_rate(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch("/organization/mileage-rate", json=body)
