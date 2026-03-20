from __future__ import annotations
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Reports:
    """Access reports."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def trial_balance(self, **params: Any) -> Any:
        return self._client.get("/reports/trial-balance", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def balance_sheet(self, **params: Any) -> Any:
        return self._client.get("/reports/balance-sheet", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def income_statement(self, **params: Any) -> Any:
        return self._client.get("/reports/income-statement", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def profit_and_loss(self, **params: Any) -> Any:
        return self._client.get("/reports/profit-and-loss", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def cash_flow(self, **params: Any) -> Any:
        return self._client.get("/reports/cash-flow", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def general_ledger(self, **params: Any) -> Any:
        return self._client.get("/reports/general-ledger", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def aged_receivables(self, **params: Any) -> Any:
        return self._client.get("/reports/aged-receivables", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def aged_payables(self, **params: Any) -> Any:
        return self._client.get("/reports/aged-payables", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def account_transactions(self, **params: Any) -> Any:
        return self._client.get("/reports/account-transactions", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def bank_cash_flow(self, **params: Any) -> Any:
        return self._client.get("/reports/bank-cash-flow", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def expense_analytics(self, **params: Any) -> Any:
        return self._client.get("/reports/expense-analytics", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def financial_ratios(self, **params: Any) -> Any:
        return self._client.get("/reports/financial-ratios", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def recurring_transactions(self, **params: Any) -> Any:
        return self._client.get("/reports/recurring-transactions", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def vendor_spend(self, **params: Any) -> Any:
        return self._client.get("/reports/vendor-spend", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def sales_tax(self, **params: Any) -> Any:
        return self._client.get("/reports/sales-tax", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def vat_return(self, **params: Any) -> Any:
        return self._client.get("/reports/vat-return", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def bas(self, **params: Any) -> Any:
        return self._client.get("/reports/bas", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def schedule_c(self, **params: Any) -> Any:
        return self._client.get("/reports/schedule-c", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def budget_vs_actual(self, **params: Any) -> Any:
        return self._client.get("/reports/budget-vs-actual", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def run(
        self,
        *,
        data_source: str,
        filters: Optional[Dict[str, Any]] = None,
        group_by: Optional[List[str]] = None,
        columns: Optional[List[str]] = None,
        date_range: Optional[Dict[str, str]] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "dataSource": data_source,
            "filters": filters,
            "groupBy": group_by,
            "columns": columns,
            "dateRange": date_range,
        }
        return self._client.post("/reports/run", json={k: v for k, v in body.items() if v is not None})

    def list_saved(self) -> Any:
        return self._client.get("/reports/saved")

    def save(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/reports/saved", json=body)

    def list_schedules(self) -> Any:
        return self._client.get("/reports/schedules")

    def create_schedule(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/reports/schedules", json=body)

    def cash_flow_forecast(self, **params: Any) -> Any:
        return self._client.get("/reports/cash-flow-forecast", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def payment_performance(self, **params: Any) -> Any:
        return self._client.get("/reports/payment-performance", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def tax_summary(self, **params: Any) -> Any:
        return self._client.get("/reports/tax-summary", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def profitability(self, **params: Any) -> Any:
        return self._client.get("/reports/profitability", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def pnl_comparison(self, **params: Any) -> Any:
        return self._client.get("/reports/pnl-comparison", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def monthly_trends(self, **params: Any) -> Any:
        return self._client.get("/reports/monthly-trends", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def duplicate_detection(self, **params: Any) -> Any:
        return self._client.get("/reports/duplicate-detection", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def inventory_valuation(self, **params: Any) -> Any:
        return self._client.get("/reports/inventory-valuation", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def financial_calendar(self, **params: Any) -> Any:
        return self._client.get("/reports/financial-calendar", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def bank_reconciliation_status(self, **params: Any) -> Any:
        return self._client.get("/reports/bank-reconciliation-status", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def unrealized_gains_losses(self, **params: Any) -> Any:
        return self._client.get("/reports/unrealized-gains-losses", params={_to_camel(k): v for k, v in params.items() if v is not None})

    def export_saved_report(self, report_id: str, **params: Any) -> Any:
        return self._client.get(f"/reports/saved/{report_id}/export", params={_to_camel(k): v for k, v in params.items() if v is not None})


class AsyncReports:
    """Access reports (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def trial_balance(self, **params: Any) -> Any:
        return await self._client.get("/reports/trial-balance", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def balance_sheet(self, **params: Any) -> Any:
        return await self._client.get("/reports/balance-sheet", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def income_statement(self, **params: Any) -> Any:
        return await self._client.get("/reports/income-statement", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def profit_and_loss(self, **params: Any) -> Any:
        return await self._client.get("/reports/profit-and-loss", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def cash_flow(self, **params: Any) -> Any:
        return await self._client.get("/reports/cash-flow", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def general_ledger(self, **params: Any) -> Any:
        return await self._client.get("/reports/general-ledger", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def aged_receivables(self, **params: Any) -> Any:
        return await self._client.get("/reports/aged-receivables", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def aged_payables(self, **params: Any) -> Any:
        return await self._client.get("/reports/aged-payables", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def account_transactions(self, **params: Any) -> Any:
        return await self._client.get("/reports/account-transactions", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def bank_cash_flow(self, **params: Any) -> Any:
        return await self._client.get("/reports/bank-cash-flow", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def expense_analytics(self, **params: Any) -> Any:
        return await self._client.get("/reports/expense-analytics", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def financial_ratios(self, **params: Any) -> Any:
        return await self._client.get("/reports/financial-ratios", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def recurring_transactions(self, **params: Any) -> Any:
        return await self._client.get("/reports/recurring-transactions", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def vendor_spend(self, **params: Any) -> Any:
        return await self._client.get("/reports/vendor-spend", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def sales_tax(self, **params: Any) -> Any:
        return await self._client.get("/reports/sales-tax", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def vat_return(self, **params: Any) -> Any:
        return await self._client.get("/reports/vat-return", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def bas(self, **params: Any) -> Any:
        return await self._client.get("/reports/bas", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def schedule_c(self, **params: Any) -> Any:
        return await self._client.get("/reports/schedule-c", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def budget_vs_actual(self, **params: Any) -> Any:
        return await self._client.get("/reports/budget-vs-actual", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def run(
        self,
        *,
        data_source: str,
        filters: Optional[Dict[str, Any]] = None,
        group_by: Optional[List[str]] = None,
        columns: Optional[List[str]] = None,
        date_range: Optional[Dict[str, str]] = None,
    ) -> Any:
        body: Dict[str, Any] = {
            "dataSource": data_source,
            "filters": filters,
            "groupBy": group_by,
            "columns": columns,
            "dateRange": date_range,
        }
        return await self._client.post("/reports/run", json={k: v for k, v in body.items() if v is not None})

    async def list_saved(self) -> Any:
        return await self._client.get("/reports/saved")

    async def save(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/reports/saved", json=body)

    async def list_schedules(self) -> Any:
        return await self._client.get("/reports/schedules")

    async def create_schedule(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/reports/schedules", json=body)

    async def cash_flow_forecast(self, **params: Any) -> Any:
        return await self._client.get("/reports/cash-flow-forecast", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def payment_performance(self, **params: Any) -> Any:
        return await self._client.get("/reports/payment-performance", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def tax_summary(self, **params: Any) -> Any:
        return await self._client.get("/reports/tax-summary", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def profitability(self, **params: Any) -> Any:
        return await self._client.get("/reports/profitability", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def pnl_comparison(self, **params: Any) -> Any:
        return await self._client.get("/reports/pnl-comparison", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def monthly_trends(self, **params: Any) -> Any:
        return await self._client.get("/reports/monthly-trends", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def duplicate_detection(self, **params: Any) -> Any:
        return await self._client.get("/reports/duplicate-detection", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def inventory_valuation(self, **params: Any) -> Any:
        return await self._client.get("/reports/inventory-valuation", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def financial_calendar(self, **params: Any) -> Any:
        return await self._client.get("/reports/financial-calendar", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def bank_reconciliation_status(self, **params: Any) -> Any:
        return await self._client.get("/reports/bank-reconciliation-status", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def unrealized_gains_losses(self, **params: Any) -> Any:
        return await self._client.get("/reports/unrealized-gains-losses", params={_to_camel(k): v for k, v in params.items() if v is not None})

    async def export_saved_report(self, report_id: str, **params: Any) -> Any:
        return await self._client.get(f"/reports/saved/{report_id}/export", params={_to_camel(k): v for k, v in params.items() if v is not None})
