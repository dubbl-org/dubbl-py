from __future__ import annotations

from ._base_client import AsyncAPIClient, SyncAPIClient
from .resources.accounts import Accounts, AsyncAccounts
from .resources.accrual_schedules import AccrualSchedules, AsyncAccrualSchedules
from .resources.admin import Admin, AsyncAdmin
from .resources.advisors import Advisors, AsyncAdvisors
from .resources.api_keys import ApiKeys as APIKeys
from .resources.api_keys import AsyncApiKeys as AsyncAPIKeys
from .resources.approval_requests import ApprovalRequests, AsyncApprovalRequests
from .resources.approval_workflows import ApprovalWorkflows, AsyncApprovalWorkflows
from .resources.attachments import AsyncAttachments, Attachments
from .resources.audit_log import AsyncAuditLog, AuditLog
from .resources.backups import AsyncBackups, Backups
from .resources.bank_accounts import AsyncBankAccounts, BankAccounts
from .resources.bank_imports import AsyncBankImports, BankImports
from .resources.bank_rules import AsyncBankRules, BankRules
from .resources.bank_transactions import AsyncBankTransactions, BankTransactions
from .resources.billing import AsyncBilling, Billing
from .resources.bills import AsyncBills, Bills
from .resources.budgets import AsyncBudgets, Budgets
from .resources.bulk import AsyncBulk, Bulk
from .resources.consolidation import AsyncConsolidation, Consolidation
from .resources.contacts import AsyncContacts, Contacts
from .resources.cost_centers import AsyncCostCenters, CostCenters
from .resources.credit_notes import AsyncCreditNotes, CreditNotes
from .resources.crm import CRM, AsyncCRM
from .resources.currencies import AsyncCurrencies, Currencies
from .resources.dashboard import AsyncDashboard, Dashboard
from .resources.debit_notes import AsyncDebitNotes, DebitNotes
from .resources.document_emails import AsyncDocumentEmails, DocumentEmails
from .resources.document_templates import AsyncDocumentTemplates, DocumentTemplates
from .resources.documents import AsyncDocuments, Documents
from .resources.email_config import AsyncEmailConfig, EmailConfig
from .resources.entries import AsyncEntries, Entries
from .resources.exchange_rates import AsyncExchangeRates, ExchangeRates
from .resources.expenses import AsyncExpenses, Expenses
from .resources.export import AsyncExport, Export
from .resources.fiscal_years import AsyncFiscalYears, FiscalYears
from .resources.fixed_assets import AsyncFixedAssets, FixedAssets
from .resources.integrations import AsyncIntegrations, Integrations
from .resources.inventory import AsyncInventory, Inventory
from .resources.invitations import AsyncInvitations, Invitations
from .resources.invite_links import AsyncInviteLinks, InviteLinks
from .resources.invoices import AsyncInvoices, Invoices
from .resources.landed_costs import AsyncLandedCosts, LandedCosts
from .resources.loans import AsyncLoans, Loans
from .resources.members import AsyncMembers, Members
from .resources.notifications import AsyncNotifications, Notifications
from .resources.ocr import OCR, AsyncOCR
from .resources.opening_balances import AsyncOpeningBalances, OpeningBalances
from .resources.organization import AsyncOrganization, Organization
from .resources.payment_batches import AsyncPaymentBatches, PaymentBatches
from .resources.payments import AsyncPayments, Payments
from .resources.payroll import AsyncPayroll, Payroll
from .resources.period_lock import AsyncPeriodLock, PeriodLock
from .resources.portal import AsyncPortal, Portal
from .resources.projects import AsyncProjects, Projects
from .resources.purchase_orders import AsyncPurchaseOrders, PurchaseOrders
from .resources.purchase_requisitions import AsyncPurchaseRequisitions, PurchaseRequisitions
from .resources.quotes import AsyncQuotes, Quotes
from .resources.recurring import AsyncRecurring, Recurring
from .resources.reminder_rules import AsyncReminderRules, ReminderRules
from .resources.reminders import AsyncReminders, Reminders
from .resources.report_schedules import AsyncReportSchedules, ReportSchedules
from .resources.reports import AsyncReports, Reports
from .resources.revenue_schedules import AsyncRevenueSchedules, RevenueSchedules
from .resources.roles import AsyncRoles, Roles
from .resources.scheduled_payments import AsyncScheduledPayments, ScheduledPayments
from .resources.sessions import AsyncSessions, Sessions
from .resources.stock_takes import AsyncStockTakes, StockTakes
from .resources.tags import AsyncTags, Tags
from .resources.tax_lookup import AsyncTaxLookup, TaxLookup
from .resources.tax_periods import AsyncTaxPeriods, TaxPeriods
from .resources.tax_rates import AsyncTaxRates, TaxRates
from .resources.teams import AsyncTeams, Teams
from .resources.trash import AsyncTrash, Trash
from .resources.user import AsyncUser, User
from .resources.warehouses import AsyncWarehouses, Warehouses
from .resources.webhooks import AsyncWebhooks, Webhooks
from .resources.workflows import AsyncWorkflows, Workflows


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
        api_key: str | None = None,
        base_url: str | None = None,
        organization_id: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        default_headers: dict[str, str] | None = None,
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
        self.admin = Admin(self._client)
        self.entries = Entries(self._client)
        self.invoices = Invoices(self._client)
        self.bills = Bills(self._client)
        self.contacts = Contacts(self._client)
        self.currencies = Currencies(self._client)
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
        self.integrations = Integrations(self._client)
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
        self.payroll = Payroll(self._client)
        self.crm = CRM(self._client)
        self.bulk = Bulk(self._client)
        self.consolidation = Consolidation(self._client)
        self.dashboard = Dashboard(self._client)
        self.debit_notes = DebitNotes(self._client)
        self.document_emails = DocumentEmails(self._client)
        self.document_templates = DocumentTemplates(self._client)
        self.email_config = EmailConfig(self._client)
        self.exchange_rates = ExchangeRates(self._client)
        self.bank_rules = BankRules(self._client)
        self.bank_imports = BankImports(self._client)
        self.approval_workflows = ApprovalWorkflows(self._client)
        self.approval_requests = ApprovalRequests(self._client)
        self.notifications = Notifications(self._client)
        self.ocr = OCR(self._client)
        self.opening_balances = OpeningBalances(self._client)
        self.payment_batches = PaymentBatches(self._client)
        self.period_lock = PeriodLock(self._client)
        self.portal = Portal(self._client)
        self.purchase_requisitions = PurchaseRequisitions(self._client)
        self.reminders = Reminders(self._client)
        self.reminder_rules = ReminderRules(self._client)
        self.report_schedules = ReportSchedules(self._client)
        self.revenue_schedules = RevenueSchedules(self._client)
        self.accrual_schedules = AccrualSchedules(self._client)
        self.scheduled_payments = ScheduledPayments(self._client)
        self.sessions = Sessions(self._client)
        self.stock_takes = StockTakes(self._client)
        self.tax_periods = TaxPeriods(self._client)
        self.teams = Teams(self._client)
        self.warehouses = Warehouses(self._client)
        self.workflows = Workflows(self._client)
        self.loans = Loans(self._client)
        self.landed_costs = LandedCosts(self._client)
        self.invitations = Invitations(self._client)
        self.invite_links = InviteLinks(self._client)
        self.advisors = Advisors(self._client)
        self.billing = Billing(self._client)
        self.tax_lookup = TaxLookup(self._client)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> Dubbl:
        return self

    def __exit__(self, *args: object) -> None:
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
        api_key: str | None = None,
        base_url: str | None = None,
        organization_id: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        default_headers: dict[str, str] | None = None,
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
        self.admin = AsyncAdmin(self._client)
        self.entries = AsyncEntries(self._client)
        self.invoices = AsyncInvoices(self._client)
        self.bills = AsyncBills(self._client)
        self.contacts = AsyncContacts(self._client)
        self.currencies = AsyncCurrencies(self._client)
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
        self.integrations = AsyncIntegrations(self._client)
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
        self.payroll = AsyncPayroll(self._client)
        self.crm = AsyncCRM(self._client)
        self.bulk = AsyncBulk(self._client)
        self.consolidation = AsyncConsolidation(self._client)
        self.dashboard = AsyncDashboard(self._client)
        self.debit_notes = AsyncDebitNotes(self._client)
        self.document_emails = AsyncDocumentEmails(self._client)
        self.document_templates = AsyncDocumentTemplates(self._client)
        self.email_config = AsyncEmailConfig(self._client)
        self.exchange_rates = AsyncExchangeRates(self._client)
        self.bank_rules = AsyncBankRules(self._client)
        self.bank_imports = AsyncBankImports(self._client)
        self.approval_workflows = AsyncApprovalWorkflows(self._client)
        self.approval_requests = AsyncApprovalRequests(self._client)
        self.notifications = AsyncNotifications(self._client)
        self.ocr = AsyncOCR(self._client)
        self.opening_balances = AsyncOpeningBalances(self._client)
        self.payment_batches = AsyncPaymentBatches(self._client)
        self.period_lock = AsyncPeriodLock(self._client)
        self.portal = AsyncPortal(self._client)
        self.purchase_requisitions = AsyncPurchaseRequisitions(self._client)
        self.reminders = AsyncReminders(self._client)
        self.reminder_rules = AsyncReminderRules(self._client)
        self.report_schedules = AsyncReportSchedules(self._client)
        self.revenue_schedules = AsyncRevenueSchedules(self._client)
        self.accrual_schedules = AsyncAccrualSchedules(self._client)
        self.scheduled_payments = AsyncScheduledPayments(self._client)
        self.sessions = AsyncSessions(self._client)
        self.stock_takes = AsyncStockTakes(self._client)
        self.tax_periods = AsyncTaxPeriods(self._client)
        self.teams = AsyncTeams(self._client)
        self.warehouses = AsyncWarehouses(self._client)
        self.workflows = AsyncWorkflows(self._client)
        self.loans = AsyncLoans(self._client)
        self.landed_costs = AsyncLandedCosts(self._client)
        self.invitations = AsyncInvitations(self._client)
        self.invite_links = AsyncInviteLinks(self._client)
        self.advisors = AsyncAdvisors(self._client)
        self.billing = AsyncBilling(self._client)
        self.tax_lookup = AsyncTaxLookup(self._client)

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._client.close()

    async def __aenter__(self) -> AsyncDubbl:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
