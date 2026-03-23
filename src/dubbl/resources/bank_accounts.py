from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class BankAccounts:
    """Manage bank accounts."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/bank-accounts", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def create(
        self,
        *,
        account_name: str,
        account_number: str | None = None,
        bank_name: str | None = None,
        currency_code: str | None = None,
        country_code: str | None = None,
        account_type: str | None = None,
        color: str | None = None,
        chart_account_id: str | None = None,
        balance: JSONValue | None = None,
    ) -> ResponseValue:
        body: dict[str, JSONValue] = {
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

    def retrieve(self, bank_account_id: str) -> ResponseValue:
        return self._client.get(f"/bank-accounts/{bank_account_id}")

    def update(self, bank_account_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/bank-accounts/{bank_account_id}", json=body)

    def delete(self, bank_account_id: str) -> ResponseValue:
        return self._client.delete(f"/bank-accounts/{bank_account_id}")

    def import_transactions(self, bank_account_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/bank-accounts/{bank_account_id}/transactions/import", json=body)

    def sync(self, bank_account_id: str) -> ResponseValue:
        raise NotImplementedError("The current v1 API does not expose bank account sync; use imports or integrations.")

    def list_transactions(self, bank_account_id: str, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            f"/bank-accounts/{bank_account_id}/transactions",
            params={_to_camel(k): v for k, v in params.items() if v is not None},
        )

    def list_reconciliations(self, bank_account_id: str) -> ResponseValue:
        return self._client.get(f"/bank-accounts/{bank_account_id}/reconciliations")

    def list_imports(self, bank_account_id: str) -> ResponseValue:
        return self._client.get(f"/bank-accounts/{bank_account_id}/imports")

    def find_duplicates(self, bank_account_id: str) -> ResponseValue:
        return self._client.get(f"/bank-accounts/{bank_account_id}/duplicates")

    def validate_balance(self, bank_account_id: str) -> ResponseValue:
        return self._client.get(f"/bank-accounts/{bank_account_id}/validate-balance")


class AsyncBankAccounts:
    """Manage bank accounts (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/bank-accounts", params={_to_camel(k): v for k, v in params.items() if v is not None}
        )

    async def create(
        self,
        *,
        account_name: str,
        account_number: str | None = None,
        bank_name: str | None = None,
        currency_code: str | None = None,
        country_code: str | None = None,
        account_type: str | None = None,
        color: str | None = None,
        chart_account_id: str | None = None,
        balance: JSONValue | None = None,
    ) -> ResponseValue:
        body: dict[str, JSONValue] = {
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

    async def retrieve(self, bank_account_id: str) -> ResponseValue:
        return await self._client.get(f"/bank-accounts/{bank_account_id}")

    async def update(self, bank_account_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/bank-accounts/{bank_account_id}", json=body)

    async def delete(self, bank_account_id: str) -> ResponseValue:
        return await self._client.delete(f"/bank-accounts/{bank_account_id}")

    async def import_transactions(self, bank_account_id: str, **kwargs: JSONValue) -> ResponseValue:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/bank-accounts/{bank_account_id}/transactions/import", json=body)

    async def sync(self, bank_account_id: str) -> ResponseValue:
        raise NotImplementedError("The current v1 API does not expose bank account sync; use imports or integrations.")

    async def list_transactions(self, bank_account_id: str, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            f"/bank-accounts/{bank_account_id}/transactions",
            params={_to_camel(k): v for k, v in params.items() if v is not None},
        )

    async def list_reconciliations(self, bank_account_id: str) -> ResponseValue:
        return await self._client.get(f"/bank-accounts/{bank_account_id}/reconciliations")

    async def list_imports(self, bank_account_id: str) -> ResponseValue:
        return await self._client.get(f"/bank-accounts/{bank_account_id}/imports")

    async def find_duplicates(self, bank_account_id: str) -> ResponseValue:
        return await self._client.get(f"/bank-accounts/{bank_account_id}/duplicates")

    async def validate_balance(self, bank_account_id: str) -> ResponseValue:
        return await self._client.get(f"/bank-accounts/{bank_account_id}/validate-balance")
