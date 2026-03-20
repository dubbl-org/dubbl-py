from __future__ import annotations
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Contacts:
    """Manage contacts."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        search: Optional[str] = None,
        type: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Any:
        params: Dict[str, Any] = {
            "search": search,
            "type": type,
            "from": from_date,
            "to": to_date,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "page": page,
            "limit": limit,
        }
        return self._client.get("/contacts", params=params)

    def create(
        self,
        *,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        tax_number: Optional[str] = None,
        type: Optional[str] = None,
        payment_terms_days: Optional[int] = None,
        addresses: Optional[List[Dict[str, Any]]] = None,
        notes: Optional[str] = None,
        currency_code: Optional[str] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "name": name,
            "email": email,
            "phone": phone,
            "taxNumber": tax_number,
            "type": type,
            "paymentTermsDays": payment_terms_days,
            "addresses": addresses,
            "notes": notes,
            "currencyCode": currency_code,
        }
        return self._client.post("/contacts", json={k: v for k, v in body.items() if v is not None})

    def retrieve(self, contact_id: str) -> Any:
        return self._client.get(f"/contacts/{contact_id}")

    def update(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/contacts/{contact_id}", json=body)

    def delete(self, contact_id: str) -> Any:
        return self._client.delete(f"/contacts/{contact_id}")

    def list_people(self, contact_id: str) -> Any:
        return self._client.get(f"/contacts/{contact_id}/people")

    def create_person(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/contacts/{contact_id}/people", json=body)

    def statement(self, contact_id: str, **kwargs: Any) -> Any:
        params = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.get(f"/contacts/{contact_id}/statement", params=params)

    def statement_pdf(self, contact_id: str, **kwargs: Any) -> Any:
        params = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.get(f"/contacts/{contact_id}/statement/pdf", params=params, raw_response=True)

    def send_statement(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/contacts/{contact_id}/statement/send", json=body)

    def activity(self, contact_id: str) -> Any:
        return self._client.get(f"/contacts/{contact_id}/activity")

    def list_files(self, contact_id: str) -> Any:
        return self._client.get(f"/contacts/{contact_id}/files")

    def upload_file(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/contacts/{contact_id}/files", json=body)


class AsyncContacts:
    """Manage contacts (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        search: Optional[str] = None,
        type: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Any:
        params: Dict[str, Any] = {
            "search": search,
            "type": type,
            "from": from_date,
            "to": to_date,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "page": page,
            "limit": limit,
        }
        return await self._client.get("/contacts", params=params)

    async def create(
        self,
        *,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        tax_number: Optional[str] = None,
        type: Optional[str] = None,
        payment_terms_days: Optional[int] = None,
        addresses: Optional[List[Dict[str, Any]]] = None,
        notes: Optional[str] = None,
        currency_code: Optional[str] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "name": name,
            "email": email,
            "phone": phone,
            "taxNumber": tax_number,
            "type": type,
            "paymentTermsDays": payment_terms_days,
            "addresses": addresses,
            "notes": notes,
            "currencyCode": currency_code,
        }
        return await self._client.post("/contacts", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, contact_id: str) -> Any:
        return await self._client.get(f"/contacts/{contact_id}")

    async def update(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/contacts/{contact_id}", json=body)

    async def delete(self, contact_id: str) -> Any:
        return await self._client.delete(f"/contacts/{contact_id}")

    async def list_people(self, contact_id: str) -> Any:
        return await self._client.get(f"/contacts/{contact_id}/people")

    async def create_person(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/contacts/{contact_id}/people", json=body)

    async def statement(self, contact_id: str, **kwargs: Any) -> Any:
        params = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.get(f"/contacts/{contact_id}/statement", params=params)

    async def statement_pdf(self, contact_id: str, **kwargs: Any) -> Any:
        params = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.get(f"/contacts/{contact_id}/statement/pdf", params=params, raw_response=True)

    async def send_statement(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/contacts/{contact_id}/statement/send", json=body)

    async def activity(self, contact_id: str) -> Any:
        return await self._client.get(f"/contacts/{contact_id}/activity")

    async def list_files(self, contact_id: str) -> Any:
        return await self._client.get(f"/contacts/{contact_id}/files")

    async def upload_file(self, contact_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/contacts/{contact_id}/files", json=body)
