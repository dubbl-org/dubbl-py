from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class BankAccounts:
    """Manage bank accounts."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/bank-accounts", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(
        self,
        *,
        account_name: str,
        account_number: Optional[str] = None,
        bank_name: Optional[str] = None,
        currency_code: Optional[str] = None,
        country_code: Optional[str] = None,
        account_type: Optional[str] = None,
        color: Optional[str] = None,
        chart_account_id: Optional[str] = None,
        balance: Optional[Any] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "accountName": account_name,
            "accountNumber": account_number,
            "bankName": bank_name,
            "currencyCode": currency_code,
            "countryCode": country_code,
            "accountType": account_type,
            "color": color,
            "chartAccountId": chart_account_id,
            "balance": balance,
        }
        return self._client.post("/bank-accounts", json={k: v for k, v in body.items() if v is not None})

    def retrieve(self, bank_account_id: str) -> Any:
        return self._client.get(f"/bank-accounts/{bank_account_id}")

    def update(self, bank_account_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/bank-accounts/{bank_account_id}", json=body)

    def delete(self, bank_account_id: str) -> Any:
        return self._client.delete(f"/bank-accounts/{bank_account_id}")

    def import_transactions(self, bank_account_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-accounts/{bank_account_id}/import", json=body)

    def sync(self, bank_account_id: str) -> Any:
        return self._client.post(f"/bank-accounts/{bank_account_id}/sync")


class AsyncBankAccounts:
    """Manage bank accounts (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/bank-accounts", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def create(
        self,
        *,
        account_name: str,
        account_number: Optional[str] = None,
        bank_name: Optional[str] = None,
        currency_code: Optional[str] = None,
        country_code: Optional[str] = None,
        account_type: Optional[str] = None,
        color: Optional[str] = None,
        chart_account_id: Optional[str] = None,
        balance: Optional[Any] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "accountName": account_name,
            "accountNumber": account_number,
            "bankName": bank_name,
            "currencyCode": currency_code,
            "countryCode": country_code,
            "accountType": account_type,
            "color": color,
            "chartAccountId": chart_account_id,
            "balance": balance,
        }
        return await self._client.post("/bank-accounts", json={k: v for k, v in body.items() if v is not None})

    async def retrieve(self, bank_account_id: str) -> Any:
        return await self._client.get(f"/bank-accounts/{bank_account_id}")

    async def update(self, bank_account_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/bank-accounts/{bank_account_id}", json=body)

    async def delete(self, bank_account_id: str) -> Any:
        return await self._client.delete(f"/bank-accounts/{bank_account_id}")

    async def import_transactions(self, bank_account_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-accounts/{bank_account_id}/import", json=body)

    async def sync(self, bank_account_id: str) -> Any:
        return await self._client.post(f"/bank-accounts/{bank_account_id}/sync")
