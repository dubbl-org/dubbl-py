from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class CRM:
    """CRM management - deals, pipelines, activities, analytics."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    # Analytics
    def get_analytics(self, **params: Any) -> Any:
        return self._client.get("/crm/analytics", params={k: v for k, v in params.items() if v is not None})

    # Deals
    def list_deals(self, **params: Any) -> Any:
        return self._client.get("/crm/deals", params={k: v for k, v in params.items() if v is not None})

    def create_deal(self, **kwargs: Any) -> Any:
        return self._client.post("/crm/deals", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve_deal(self, deal_id: str) -> Any:
        return self._client.get(f"/crm/deals/{deal_id}")

    def update_deal(self, deal_id: str, **kwargs: Any) -> Any:
        return self._client.patch(
            f"/crm/deals/{deal_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_deal(self, deal_id: str) -> Any:
        return self._client.delete(f"/crm/deals/{deal_id}")

    def mark_deal_won(self, deal_id: str) -> Any:
        return self._client.post(f"/crm/deals/{deal_id}/won")

    def mark_deal_lost(self, deal_id: str) -> Any:
        return self._client.post(f"/crm/deals/{deal_id}/lost")

    def update_deal_stage(self, deal_id: str, **kwargs: Any) -> Any:
        return self._client.patch(
            f"/crm/deals/{deal_id}/stage", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def list_deal_activities(self, deal_id: str) -> Any:
        return self._client.get(f"/crm/deals/{deal_id}/activities")

    def create_deal_activity(self, deal_id: str, **kwargs: Any) -> Any:
        return self._client.post(
            f"/crm/deals/{deal_id}/activities", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Pipelines
    def list_pipelines(self, **params: Any) -> Any:
        return self._client.get("/crm/pipelines", params={k: v for k, v in params.items() if v is not None})

    def create_pipeline(self, **kwargs: Any) -> Any:
        return self._client.post("/crm/pipelines", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve_pipeline(self, pipeline_id: str) -> Any:
        return self._client.get(f"/crm/pipelines/{pipeline_id}")

    def update_pipeline(self, pipeline_id: str, **kwargs: Any) -> Any:
        return self._client.patch(
            f"/crm/pipelines/{pipeline_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_pipeline(self, pipeline_id: str) -> Any:
        return self._client.delete(f"/crm/pipelines/{pipeline_id}")


class AsyncCRM:
    """CRM management - deals, pipelines, activities, analytics."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    # Analytics
    async def get_analytics(self, **params: Any) -> Any:
        return await self._client.get("/crm/analytics", params={k: v for k, v in params.items() if v is not None})

    # Deals
    async def list_deals(self, **params: Any) -> Any:
        return await self._client.get("/crm/deals", params={k: v for k, v in params.items() if v is not None})

    async def create_deal(self, **kwargs: Any) -> Any:
        return await self._client.post("/crm/deals", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve_deal(self, deal_id: str) -> Any:
        return await self._client.get(f"/crm/deals/{deal_id}")

    async def update_deal(self, deal_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/crm/deals/{deal_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_deal(self, deal_id: str) -> Any:
        return await self._client.delete(f"/crm/deals/{deal_id}")

    async def mark_deal_won(self, deal_id: str) -> Any:
        return await self._client.post(f"/crm/deals/{deal_id}/won")

    async def mark_deal_lost(self, deal_id: str) -> Any:
        return await self._client.post(f"/crm/deals/{deal_id}/lost")

    async def update_deal_stage(self, deal_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/crm/deals/{deal_id}/stage", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def list_deal_activities(self, deal_id: str) -> Any:
        return await self._client.get(f"/crm/deals/{deal_id}/activities")

    async def create_deal_activity(self, deal_id: str, **kwargs: Any) -> Any:
        return await self._client.post(
            f"/crm/deals/{deal_id}/activities", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Pipelines
    async def list_pipelines(self, **params: Any) -> Any:
        return await self._client.get("/crm/pipelines", params={k: v for k, v in params.items() if v is not None})

    async def create_pipeline(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/crm/pipelines", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_pipeline(self, pipeline_id: str) -> Any:
        return await self._client.get(f"/crm/pipelines/{pipeline_id}")

    async def update_pipeline(self, pipeline_id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/crm/pipelines/{pipeline_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_pipeline(self, pipeline_id: str) -> Any:
        return await self._client.delete(f"/crm/pipelines/{pipeline_id}")
