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
from .resources.payroll import Payroll, AsyncPayroll
from .resources.crm import CRM, AsyncCRM
from .resources.bulk import Bulk, AsyncBulk
from .resources.consolidation import Consolidation, AsyncConsolidation
from .resources.dashboard import Dashboard, AsyncDashboard
from .resources.debit_notes import DebitNotes, AsyncDebitNotes
from .resources.document_emails import DocumentEmails, AsyncDocumentEmails
from .resources.document_templates import DocumentTemplates, AsyncDocumentTemplates
from .resources.email_config import EmailConfig, AsyncEmailConfig
from .resources.exchange_rates import ExchangeRates, AsyncExchangeRates
from .resources.bank_rules import BankRules, AsyncBankRules
from .resources.bank_imports import BankImports, AsyncBankImports
from .resources.approval_workflows import ApprovalWorkflows, AsyncApprovalWorkflows
from .resources.approval_requests import ApprovalRequests, AsyncApprovalRequests
from .resources.notifications import Notifications, AsyncNotifications
from .resources.ocr import OCR, AsyncOCR
from .resources.opening_balances import OpeningBalances, AsyncOpeningBalances
from .resources.payment_batches import PaymentBatches, AsyncPaymentBatches
from .resources.period_lock import PeriodLock, AsyncPeriodLock
from .resources.portal import Portal, AsyncPortal
from .resources.purchase_requisitions import PurchaseRequisitions, AsyncPurchaseRequisitions
from .resources.reminders import Reminders, AsyncReminders
from .resources.reminder_rules import ReminderRules, AsyncReminderRules
from .resources.report_schedules import ReportSchedules, AsyncReportSchedules
from .resources.revenue_schedules import RevenueSchedules, AsyncRevenueSchedules
from .resources.accrual_schedules import AccrualSchedules, AsyncAccrualSchedules
from .resources.scheduled_payments import ScheduledPayments, AsyncScheduledPayments
from .resources.sessions import Sessions, AsyncSessions
from .resources.stock_takes import StockTakes, AsyncStockTakes
from .resources.tax_periods import TaxPeriods, AsyncTaxPeriods
from .resources.teams import Teams, AsyncTeams
from .resources.warehouses import Warehouses, AsyncWarehouses
from .resources.workflows import Workflows, AsyncWorkflows
from .resources.loans import Loans, AsyncLoans
from .resources.landed_costs import LandedCosts, AsyncLandedCosts
from .resources.invitations import Invitations, AsyncInvitations
from .resources.invite_links import InviteLinks, AsyncInviteLinks
from .resources.advisors import Advisors, AsyncAdvisors
from .resources.billing import Billing, AsyncBilling
from .resources.tax_lookup import TaxLookup, AsyncTaxLookup


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

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
