from __future__ import annotations

import builtins
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Invoices:
    """Manage invoices."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        search: str | None = None,
        status: str | None = None,
        contact_id: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Any:
        params: dict[str, Any] = {
            "search": search,
            "status": status,
            "contactId": contact_id,
            "from": from_date,
            "to": to_date,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "page": page,
            "limit": limit,
        }
        return self._client.get("/invoices", params=params)

    def create(
        self,
        *,
        contact_id: str,
        issue_date: str,
        due_date: str | None = None,
        reference: str | None = None,
        notes: str | None = None,
        currency_code: str | None = None,
        lines: builtins.list[dict[str, Any]] | None = None,
    ) -> Any:
        body: dict[str, Any] = {
            "contactId": contact_id,
            "issueDate": issue_date,
            "dueDate": due_date,
            "reference": reference,
            "notes": notes,
            "currencyCode": currency_code,
            "lines": lines,
        }
        return self._client.post("/invoices", json={k: v for k, v in body.items() if v is not None})

    def retrieve(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}")

    def update(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/invoices/{invoice_id}", json=body)

    def delete(self, invoice_id: str) -> Any:
        return self._client.delete(f"/invoices/{invoice_id}")

    def send(self, invoice_id: str) -> Any:
        return self._client.post(f"/invoices/{invoice_id}/send")

    def void(self, invoice_id: str) -> Any:
        return self._client.post(f"/invoices/{invoice_id}/void")

    def pay(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/invoices/{invoice_id}/pay", json=body)

    def pdf(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}/pdf", raw_response=True)

    def ubl(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}/ubl")

    def summary(self) -> Any:
        return self._client.get("/invoices/summary")

    def calculate_interest(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/invoices/calculate-interest", json=body)

    def charge_interest(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/invoices/{invoice_id}/charge-interest", json=body)

    def payment_link(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}/payment-link")

    def signature_get(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}/signature")

    def signature_create(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/invoices/{invoice_id}/signature", json=body)

    def snapshot(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}/snapshot")

    def compliance(self, invoice_id: str) -> Any:
        return self._client.get(f"/invoices/{invoice_id}/compliance")

    def resend_signature(self, invoice_id: str) -> Any:
        return self._client.post(f"/invoices/{invoice_id}/signature/resend")


class AsyncInvoices:
    """Manage invoices (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        search: str | None = None,
        status: str | None = None,
        contact_id: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Any:
        params: dict[str, Any] = {
            "search": search,
            "status": status,
            "contactId": contact_id,
            "from": from_date,
            "to": to_date,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "page": page,
            "limit": limit,
        }
        return await self._client.get("/invoices", params=params)

    async def create(
        self,
        *,
        contact_id: str,
        issue_date: str,
        due_date: str | None = None,
        reference: str | None = None,
        notes: str | None = None,
        currency_code: str | None = None,
        lines: builtins.list[dict[str, Any]] | None = None,
    ) -> Any:
        body: dict[str, Any] = {
            "contactId": contact_id,
            "issueDate": issue_date,
            "dueDate": due_date,
            "reference": reference,
            "notes": notes,
            "currencyCode": currency_code,
            "lines": lines,
        }
        return await self._client.post("/invoices", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}")

    async def update(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/invoices/{invoice_id}", json=body)

    async def delete(self, invoice_id: str) -> Any:
        return await self._client.delete(f"/invoices/{invoice_id}")

    async def send(self, invoice_id: str) -> Any:
        return await self._client.post(f"/invoices/{invoice_id}/send")

    async def void(self, invoice_id: str) -> Any:
        return await self._client.post(f"/invoices/{invoice_id}/void")

    async def pay(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/invoices/{invoice_id}/pay", json=body)

    async def pdf(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}/pdf", raw_response=True)

    async def ubl(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}/ubl")

    async def summary(self) -> Any:
        return await self._client.get("/invoices/summary")

    async def calculate_interest(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/invoices/calculate-interest", json=body)

    async def charge_interest(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/invoices/{invoice_id}/charge-interest", json=body)

    async def payment_link(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}/payment-link")

    async def signature_get(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}/signature")

    async def signature_create(self, invoice_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/invoices/{invoice_id}/signature", json=body)

    async def snapshot(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}/snapshot")

    async def compliance(self, invoice_id: str) -> Any:
        return await self._client.get(f"/invoices/{invoice_id}/compliance")

    async def resend_signature(self, invoice_id: str) -> Any:
        return await self._client.post(f"/invoices/{invoice_id}/signature/resend")
