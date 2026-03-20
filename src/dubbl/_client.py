from __future__ import annotations

from typing import Any, Dict, Optional

from ._base_client import AsyncAPIClient, SyncAPIClient
from .resources.accounts import Accounts, AsyncAccounts
from .resources.entries import Entries, AsyncEntries
from .resources.invoices import Invoices, AsyncInvoices
from .resources.bills import Bills, AsyncBills
from .resources.contacts import Contacts, AsyncContacts
from .resources.payments import Payments, AsyncPayments
from .resources.bank_accounts import BankAccounts, AsyncBankAccounts
from .resources.bank_transactions import BankTransactions, AsyncBankTransactions
from .resources.quotes import Quotes, AsyncQuotes
from .resources.expenses import Expenses, AsyncExpenses
from .resources.inventory import Inventory, AsyncInventory
from .resources.organization import Organization, AsyncOrganization
from .resources.members import Members, AsyncMembers
from .resources.api_keys import ApiKeys as APIKeys, AsyncApiKeys as AsyncAPIKeys
from .resources.reports import Reports, AsyncReports
from .resources.audit_log import AuditLog, AsyncAuditLog
from .resources.tax_rates import TaxRates, AsyncTaxRates
from .resources.budgets import Budgets, AsyncBudgets
from .resources.fixed_assets import FixedAssets, AsyncFixedAssets
from .resources.projects import Projects, AsyncProjects
from .resources.cost_centers import CostCenters, AsyncCostCenters
from .resources.credit_notes import CreditNotes, AsyncCreditNotes
from .resources.purchase_orders import PurchaseOrders, AsyncPurchaseOrders
from .resources.recurring import Recurring, AsyncRecurring
from .resources.fiscal_years import FiscalYears, AsyncFiscalYears
from .resources.webhooks import Webhooks, AsyncWebhooks
from .resources.roles import Roles, AsyncRoles
from .resources.tags import Tags, AsyncTags
from .resources.documents import Documents, AsyncDocuments
from .resources.attachments import Attachments, AsyncAttachments
from .resources.trash import Trash, AsyncTrash
from .resources.export import Export, AsyncExport
from .resources.backups import Backups, AsyncBackups
from .resources.user import User, AsyncUser


class Dubbl:
    """Synchronous Dubbl API client.

    Args:
        api_key: Your Dubbl API key (or set DUBBL_API_KEY env var).
        base_url: Override the default API base URL.
        organization_id: Default organization ID for all requests.
        timeout: Request timeout in seconds (default: 60).
        max_retries: Max retry attempts for failed requests (default: 2).
        default_headers: Additional headers to include in every request.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        organization_id: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        default_headers: Optional[Dict[str, str]] = None,
    ) -> None:
        self._client = SyncAPIClient(
            api_key=api_key,
            base_url=base_url,
            organization_id=organization_id,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )

        self.accounts = Accounts(self._client)
        self.entries = Entries(self._client)
        self.invoices = Invoices(self._client)
        self.bills = Bills(self._client)
        self.contacts = Contacts(self._client)
        self.payments = Payments(self._client)
        self.bank_accounts = BankAccounts(self._client)
        self.bank_transactions = BankTransactions(self._client)
        self.quotes = Quotes(self._client)
        self.expenses = Expenses(self._client)
        self.inventory = Inventory(self._client)
        self.organization = Organization(self._client)
        self.members = Members(self._client)
        self.api_keys = APIKeys(self._client)
        self.reports = Reports(self._client)
        self.audit_log = AuditLog(self._client)
        self.tax_rates = TaxRates(self._client)
        self.budgets = Budgets(self._client)
        self.fixed_assets = FixedAssets(self._client)
        self.projects = Projects(self._client)
        self.cost_centers = CostCenters(self._client)
        self.credit_notes = CreditNotes(self._client)
        self.purchase_orders = PurchaseOrders(self._client)
        self.recurring = Recurring(self._client)
        self.fiscal_years = FiscalYears(self._client)
        self.webhooks = Webhooks(self._client)
        self.roles = Roles(self._client)
        self.tags = Tags(self._client)
        self.documents = Documents(self._client)
        self.attachments = Attachments(self._client)
        self.trash = Trash(self._client)
        self.export = Export(self._client)
        self.backups = Backups(self._client)
        self.user = User(self._client)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> Dubbl:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


class AsyncDubbl:
    """Asynchronous Dubbl API client.

    Args:
        api_key: Your Dubbl API key (or set DUBBL_API_KEY env var).
        base_url: Override the default API base URL.
        organization_id: Default organization ID for all requests.
        timeout: Request timeout in seconds (default: 60).
        max_retries: Max retry attempts for failed requests (default: 2).
        default_headers: Additional headers to include in every request.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        organization_id: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        default_headers: Optional[Dict[str, str]] = None,
    ) -> None:
        self._client = AsyncAPIClient(
            api_key=api_key,
            base_url=base_url,
            organization_id=organization_id,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )

        self.accounts = AsyncAccounts(self._client)
        self.entries = AsyncEntries(self._client)
        self.invoices = AsyncInvoices(self._client)
        self.bills = AsyncBills(self._client)
        self.contacts = AsyncContacts(self._client)
        self.payments = AsyncPayments(self._client)
        self.bank_accounts = AsyncBankAccounts(self._client)
        self.bank_transactions = AsyncBankTransactions(self._client)
        self.quotes = AsyncQuotes(self._client)
        self.expenses = AsyncExpenses(self._client)
        self.inventory = AsyncInventory(self._client)
        self.organization = AsyncOrganization(self._client)
        self.members = AsyncMembers(self._client)
        self.api_keys = AsyncAPIKeys(self._client)
        self.reports = AsyncReports(self._client)
        self.audit_log = AsyncAuditLog(self._client)
        self.tax_rates = AsyncTaxRates(self._client)
        self.budgets = AsyncBudgets(self._client)
        self.fixed_assets = AsyncFixedAssets(self._client)
        self.projects = AsyncProjects(self._client)
        self.cost_centers = AsyncCostCenters(self._client)
        self.credit_notes = AsyncCreditNotes(self._client)
        self.purchase_orders = AsyncPurchaseOrders(self._client)
        self.recurring = AsyncRecurring(self._client)
        self.fiscal_years = AsyncFiscalYears(self._client)
        self.webhooks = AsyncWebhooks(self._client)
        self.roles = AsyncRoles(self._client)
        self.tags = AsyncTags(self._client)
        self.documents = AsyncDocuments(self._client)
        self.attachments = AsyncAttachments(self._client)
        self.trash = AsyncTrash(self._client)
        self.export = AsyncExport(self._client)
        self.backups = AsyncBackups(self._client)
        self.user = AsyncUser(self._client)

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._client.close()

    async def __aenter__(self) -> AsyncDubbl:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
