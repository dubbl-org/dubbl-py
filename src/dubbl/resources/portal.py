from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Portal:
    """Manage portal access and public portal endpoints."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list_access(self, **params: Any) -> Any:
        return self._client.get("/portal/access", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def delete_access(self, access_id: str) -> Any:
        return self._client.delete(f"/portal/access/{access_id}")

    def revoke_access(self, access_id: str) -> Any:
        return self.delete_access(access_id)

    def invite(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/portal/invite", json=body)

    def get_statements(self, token: str, **params: Any) -> Any:
        return self._client.get(
            f"/portal/{token}/statements", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    def list_payments(self, token: str) -> Any:
        return self._client.get(f"/portal/{token}/payments")

    def list_quotes(self, token: str) -> Any:
        return self._client.get(f"/portal/{token}/quotes")

    def accept_quote(self, token: str, quote_id: str) -> Any:
        return self._client.post(f"/portal/{token}/quotes/{quote_id}/accept")

    def get_details(self, token: str) -> Any:
        return self._client.get(f"/api/portal/{token}")

    def list_invoices(self, token: str) -> Any:
        return self._client.get(f"/api/portal/{token}/invoices")

    def get_invoice_pdf(self, token: str, invoice_id: str) -> Any:
        return self._client.get(f"/api/portal/{token}/invoices/{invoice_id}/pdf", raw_response=True)

    def approve_invoice(self, token: str, invoice_id: str) -> Any:
        return self._client.post(f"/api/portal/{token}/invoices/{invoice_id}/approve")


class AsyncPortal:
    """Manage portal access and public portal endpoints (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list_access(self, **params: Any) -> Any:
        return await self._client.get(
            "/portal/access", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def delete_access(self, access_id: str) -> Any:
        return await self._client.delete(f"/portal/access/{access_id}")

    async def revoke_access(self, access_id: str) -> Any:
        return await self.delete_access(access_id)

    async def invite(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/portal/invite", json=body)

    async def get_statements(self, token: str, **params: Any) -> Any:
        return await self._client.get(
            f"/portal/{token}/statements", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def list_payments(self, token: str) -> Any:
        return await self._client.get(f"/portal/{token}/payments")

    async def list_quotes(self, token: str) -> Any:
        return await self._client.get(f"/portal/{token}/quotes")

    async def accept_quote(self, token: str, quote_id: str) -> Any:
        return await self._client.post(f"/portal/{token}/quotes/{quote_id}/accept")

    async def get_details(self, token: str) -> Any:
        return await self._client.get(f"/api/portal/{token}")

    async def list_invoices(self, token: str) -> Any:
        return await self._client.get(f"/api/portal/{token}/invoices")

    async def get_invoice_pdf(self, token: str, invoice_id: str) -> Any:
        return await self._client.get(f"/api/portal/{token}/invoices/{invoice_id}/pdf", raw_response=True)

    async def approve_invoice(self, token: str, invoice_id: str) -> Any:
        return await self._client.post(f"/api/portal/{token}/invoices/{invoice_id}/approve")
