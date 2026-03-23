from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Bulk:
    """Bulk operations - import, preview, and batch actions across resources."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    # Accounts
    def import_accounts(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/accounts/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_accounts(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/accounts/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Bills
    def import_bills(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/bills/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_bills(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/bills/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Bank Transactions
    def import_bank_transactions(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/bank-transactions/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_bank_transactions(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/bank-transactions/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Contacts
    def import_contacts(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/contacts/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_contacts(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/contacts/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_contacts(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/contacts/delete", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def tag_contacts(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/contacts/tag", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Entries
    def import_entries(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/entries/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_entries(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/entries/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Invoices
    def import_invoices(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/invoices/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_invoices(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/invoices/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def send_invoices(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/invoices/send", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def mark_invoices_paid(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/invoices/mark-paid", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Products
    def import_products(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/products/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_products(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/products/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Inventory
    def import_inventory(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/inventory/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def preview_inventory(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/inventory/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def adjust_inventory(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/inventory/adjust", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Transactions
    def import_transactions(self, **kwargs: Any) -> Any:
        return self.import_bank_transactions(**kwargs)

    def preview_transactions(self, **kwargs: Any) -> Any:
        return self.preview_bank_transactions(**kwargs)

    def categorize_transactions(self, **kwargs: Any) -> Any:
        return self._client.post(
            "/bulk/transactions/categorize", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Import Jobs
    def list_import_jobs(self, **params: Any) -> Any:
        return self._client.get("/bulk/import-jobs", params={k: v for k, v in params.items() if v is not None})


class AsyncBulk:
    """Bulk operations - import, preview, and batch actions across resources."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    # Accounts
    async def import_accounts(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/accounts/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_accounts(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/accounts/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Bills
    async def import_bills(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/bills/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_bills(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/bills/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Bank Transactions
    async def import_bank_transactions(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/bank-transactions/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_bank_transactions(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/bank-transactions/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Contacts
    async def import_contacts(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/contacts/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_contacts(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/contacts/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_contacts(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/contacts/delete", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def tag_contacts(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/contacts/tag", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Entries
    async def import_entries(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/entries/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_entries(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/entries/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Invoices
    async def import_invoices(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/invoices/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_invoices(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/invoices/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def send_invoices(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/invoices/send", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def mark_invoices_paid(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/invoices/mark-paid", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Products
    async def import_products(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/products/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_products(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/products/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Inventory
    async def import_inventory(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/inventory/import", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def preview_inventory(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/inventory/preview", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def adjust_inventory(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/inventory/adjust", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Transactions
    async def import_transactions(self, **kwargs: Any) -> Any:
        return await self.import_bank_transactions(**kwargs)

    async def preview_transactions(self, **kwargs: Any) -> Any:
        return await self.preview_bank_transactions(**kwargs)

    async def categorize_transactions(self, **kwargs: Any) -> Any:
        return await self._client.post(
            "/bulk/transactions/categorize", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Import Jobs
    async def list_import_jobs(self, **params: Any) -> Any:
        return await self._client.get("/bulk/import-jobs", params={k: v for k, v in params.items() if v is not None})
