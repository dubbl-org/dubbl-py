from __future__ import annotations

from typing import TYPE_CHECKING

from .._types import JSONValue, QueryValue, ResponseValue

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Payroll:
    """Payroll management - employees, runs, timesheets, leave, contractors, tax."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    # Employees
    def list_employees(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/employees", params={k: v for k, v in params.items() if v is not None})

    def create_employee(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/employees", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_employee(self, employee_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/employees/{employee_id}")

    def update_employee(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/employees/{employee_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_employee(self, employee_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/employees/{employee_id}")

    def list_employee_deductions(self, employee_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/employees/{employee_id}/deductions")

    def create_employee_deduction(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/payroll/employees/{employee_id}/deductions",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def update_employee_deduction(self, employee_id: str, deduction_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/employees/{employee_id}/deductions/{deduction_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def delete_employee_deduction(self, employee_id: str, deduction_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/employees/{employee_id}/deductions/{deduction_id}")

    def get_employee_leave_balances(self, employee_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/employees/{employee_id}/leave-balances")

    def list_employee_payslips(self, employee_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/employees/{employee_id}/payslips")

    def get_employee_schedule(self, employee_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/employees/{employee_id}/schedule")

    def update_employee_schedule(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/payroll/employees/{employee_id}/schedule",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def get_employee_tax_config(self, employee_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/employees/{employee_id}/tax-config")

    def update_employee_tax_config(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/employees/{employee_id}/tax-config",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    # Pay Runs
    def list_runs(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/runs", params={k: v for k, v in params.items() if v is not None})

    def create_run(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post("/payroll/runs", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve_run(self, run_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/runs/{run_id}")

    def update_run(self, run_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/runs/{run_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_run(self, run_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/runs/{run_id}")

    def submit_run_for_approval(self, run_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/runs/{run_id}/submit-for-approval")

    def approve_run(self, run_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/runs/{run_id}/approve")

    def reject_run(self, run_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/runs/{run_id}/reject")

    def process_run(self, run_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/runs/{run_id}/process")

    def generate_payslips(self, run_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/runs/{run_id}/generate-payslips")

    def list_run_bonuses(self, run_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/runs/{run_id}/bonuses")

    def create_run_bonus(self, run_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/payroll/runs/{run_id}/bonuses", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_run_bonus(self, run_id: str, bonus_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/runs/{run_id}/bonuses/{bonus_id}")

    def create_bonus_only_run(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/runs/bonus-only", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def create_correction_run(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/runs/correction", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def create_termination_run(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/runs/termination", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Timesheets
    def list_timesheets(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/timesheets", params={k: v for k, v in params.items() if v is not None})

    def create_timesheet(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/timesheets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_timesheet(self, timesheet_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/timesheets/{timesheet_id}")

    def update_timesheet(self, timesheet_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/timesheets/{timesheet_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_timesheet(self, timesheet_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes timesheet retrieval and updates, but not direct deletion."
        )

    def submit_timesheet(self, timesheet_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/timesheets/{timesheet_id}/submit")

    def approve_timesheet(self, timesheet_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/timesheets/{timesheet_id}/approve")

    def reject_timesheet(self, timesheet_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/timesheets/{timesheet_id}/reject")

    def list_timesheet_entries(self, timesheet_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/timesheets/{timesheet_id}/entries")

    def create_timesheet_entry(self, timesheet_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/payroll/timesheets/{timesheet_id}/entries",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    # Leave
    def list_leave_policies(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/leave/policies", params={k: v for k, v in params.items() if v is not None})

    def create_leave_policy(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/leave/policies", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_leave_policy(self, policy_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/leave/policies/{policy_id}")

    def update_leave_policy(self, policy_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/leave/policies/{policy_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_leave_policy(self, policy_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes leave policy retrieval and updates, but not direct deletion."
        )

    def list_leave_requests(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/leave/requests", params={k: v for k, v in params.items() if v is not None})

    def create_leave_request(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/leave/requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def approve_leave_request(self, request_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/leave/requests/{request_id}/approve")

    def reject_leave_request(self, request_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/leave/requests/{request_id}/reject")

    def update_leave_request(self, request_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/leave/requests/{request_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    # Contractors
    def list_contractors(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/contractors", params={k: v for k, v in params.items() if v is not None})

    def create_contractor(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/contractors", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_contractor(self, contractor_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/contractors/{contractor_id}")

    def update_contractor(self, contractor_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/contractors/{contractor_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_contractor(self, contractor_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/contractors/{contractor_id}")

    def list_contractor_payments(self, contractor_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/contractors/{contractor_id}/payments")

    def create_contractor_payment(self, contractor_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/payroll/contractors/{contractor_id}/payments",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def update_contractor_payment(self, contractor_id: str, payment_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/contractors/{contractor_id}/payments/{payment_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def process_contractor_payment(self, contractor_id: str, payment_id: str) -> ResponseValue:
        return self._client.post(f"/payroll/contractors/{contractor_id}/payments/{payment_id}/process")

    # Deduction Types
    def list_deduction_types(self) -> ResponseValue:
        return self._client.get("/payroll/deductions/types")

    def create_deduction_type(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/deductions/types", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_deduction_type(self, type_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/deductions/types/{type_id}")

    def update_deduction_type(self, type_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/deductions/types/{type_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_deduction_type(self, type_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/deductions/types/{type_id}")

    # Payslips
    def list_payslips(self, **params: QueryValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API does not expose a payslip list endpoint; use retrieve_payslip() or employee/"
            "self-service payslip methods."
        )

    def retrieve_payslip(self, payslip_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/payslips/{payslip_id}")

    def update_payslip(self, payslip_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes payslip retrieval, but not direct payslip updates."
        )

    # Shifts
    def list_shifts(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/shifts", params={k: v for k, v in params.items() if v is not None})

    def create_shift(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post("/payroll/shifts", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve_shift(self, shift_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/shifts/{shift_id}")

    def update_shift(self, shift_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/shifts/{shift_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_shift(self, shift_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/shifts/{shift_id}")

    # Tax Brackets
    def list_tax_brackets(self) -> ResponseValue:
        return self._client.get("/payroll/tax/brackets")

    def create_tax_bracket(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/tax/brackets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_tax_bracket(self, bracket_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/tax/brackets/{bracket_id}")

    def update_tax_bracket(self, bracket_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/tax/brackets/{bracket_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_tax_bracket(self, bracket_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/tax/brackets/{bracket_id}")

    # Tax Forms
    def list_tax_forms(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/tax-forms", params={k: v for k, v in params.items() if v is not None})

    def generate_tax_forms(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/tax-forms/generate", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_tax_form(self, form_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/tax-forms/{form_id}")

    def download_tax_form_pdf(self, form_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/tax-forms/{form_id}/pdf", raw_response=True)

    # Compensation
    def list_compensation_bands(self) -> ResponseValue:
        return self._client.get("/payroll/compensation/bands")

    def create_compensation_band(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/compensation/bands", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_compensation_band(self, band_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/compensation/bands/{band_id}")

    def update_compensation_band(self, band_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/compensation/bands/{band_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def delete_compensation_band(self, band_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/compensation/bands/{band_id}")

    def list_compensation_reviews(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payroll/compensation/reviews", params={k: v for k, v in params.items() if v is not None}
        )

    def create_compensation_review(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/compensation/reviews", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_compensation_review(self, review_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/compensation/reviews/{review_id}")

    def update_compensation_review(self, review_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/compensation/reviews/{review_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def list_compensation_review_entries(self, review_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/compensation/reviews/{review_id}/entries")

    def create_compensation_review_entry(self, review_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            f"/payroll/compensation/reviews/{review_id}/entries",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    def get_equity_analysis(self) -> ResponseValue:
        return self._client.get("/payroll/compensation/equity-analysis")

    # Approval Chains
    def list_approval_chains(self) -> ResponseValue:
        return self._client.get("/payroll/approval-chains")

    def create_approval_chain(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/approval-chains", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def retrieve_approval_chain(self, chain_id: str) -> ResponseValue:
        return self._client.get(f"/payroll/approval-chains/{chain_id}")

    def update_approval_chain(self, chain_id: str, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            f"/payroll/approval-chains/{chain_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def delete_approval_chain(self, chain_id: str) -> ResponseValue:
        return self._client.delete(f"/payroll/approval-chains/{chain_id}")

    # Self-Service
    def get_self_service_profile(self) -> ResponseValue:
        return self._client.get("/payroll/self-service/profile")

    def update_self_service_profile(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            "/payroll/self-service/profile", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def list_self_service_payslips(self) -> ResponseValue:
        return self._client.get("/payroll/self-service/payslips")

    def get_self_service_leave_balance(self) -> ResponseValue:
        return self._client.get("/payroll/self-service/leave-balance")

    def list_self_service_leave_requests(self) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes self-service leave request creation, but not listing via this endpoint."
        )

    def create_self_service_leave_request(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/self-service/leave-requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    def list_self_service_timesheets(self) -> ResponseValue:
        return self._client.get("/payroll/self-service/timesheets")

    def create_self_service_timesheet(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.post(
            "/payroll/self-service/timesheets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Forecasting
    def get_projection(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payroll/forecasting/projection", params={k: v for k, v in params.items() if v is not None}
        )

    def get_budget_vs_actual(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payroll/forecasting/budget-vs-actual", params={k: v for k, v in params.items() if v is not None}
        )

    def get_what_if(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payroll/forecasting/what-if", params={k: v for k, v in params.items() if v is not None}
        )

    # Reports
    def report_summary(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/reports/summary", params={k: v for k, v in params.items() if v is not None})

    def report_labor_cost(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payroll/reports/labor-cost", params={k: v for k, v in params.items() if v is not None}
        )

    def report_tax_liability(self, **params: QueryValue) -> ResponseValue:
        return self._client.get(
            "/payroll/reports/tax-liability", params={k: v for k, v in params.items() if v is not None}
        )

    def report_yoy(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/reports/yoy", params={k: v for k, v in params.items() if v is not None})

    def export_report(self, **params: QueryValue) -> ResponseValue:
        return self._client.get("/payroll/reports/export", params={k: v for k, v in params.items() if v is not None})

    # Settings
    def get_settings(self) -> ResponseValue:
        return self._client.get("/payroll/settings")

    def update_settings(self, **kwargs: JSONValue) -> ResponseValue:
        return self._client.patch(
            "/payroll/settings", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )


class AsyncPayroll:
    """Payroll management - employees, runs, timesheets, leave, contractors, tax."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    # Employees
    async def list_employees(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/employees", params={k: v for k, v in params.items() if v is not None})

    async def create_employee(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/employees", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_employee(self, employee_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/employees/{employee_id}")

    async def update_employee(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/employees/{employee_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_employee(self, employee_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/employees/{employee_id}")

    async def list_employee_deductions(self, employee_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/employees/{employee_id}/deductions")

    async def create_employee_deduction(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/payroll/employees/{employee_id}/deductions",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def update_employee_deduction(
        self, employee_id: str, deduction_id: str, **kwargs: JSONValue
    ) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/employees/{employee_id}/deductions/{deduction_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def delete_employee_deduction(self, employee_id: str, deduction_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/employees/{employee_id}/deductions/{deduction_id}")

    async def get_employee_leave_balances(self, employee_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/employees/{employee_id}/leave-balances")

    async def list_employee_payslips(self, employee_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/employees/{employee_id}/payslips")

    async def get_employee_schedule(self, employee_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/employees/{employee_id}/schedule")

    async def update_employee_schedule(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/payroll/employees/{employee_id}/schedule",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def get_employee_tax_config(self, employee_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/employees/{employee_id}/tax-config")

    async def update_employee_tax_config(self, employee_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/employees/{employee_id}/tax-config",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    # Pay Runs
    async def list_runs(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/runs", params={k: v for k, v in params.items() if v is not None})

    async def create_run(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/runs", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_run(self, run_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/runs/{run_id}")

    async def update_run(self, run_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/runs/{run_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_run(self, run_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/runs/{run_id}")

    async def submit_run_for_approval(self, run_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/runs/{run_id}/submit-for-approval")

    async def approve_run(self, run_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/runs/{run_id}/approve")

    async def reject_run(self, run_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/runs/{run_id}/reject")

    async def process_run(self, run_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/runs/{run_id}/process")

    async def generate_payslips(self, run_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/runs/{run_id}/generate-payslips")

    async def list_run_bonuses(self, run_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/runs/{run_id}/bonuses")

    async def create_run_bonus(self, run_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/payroll/runs/{run_id}/bonuses", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_run_bonus(self, run_id: str, bonus_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/runs/{run_id}/bonuses/{bonus_id}")

    async def create_bonus_only_run(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/runs/bonus-only", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def create_correction_run(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/runs/correction", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def create_termination_run(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/runs/termination", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Timesheets
    async def list_timesheets(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/timesheets", params={k: v for k, v in params.items() if v is not None})

    async def create_timesheet(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/timesheets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_timesheet(self, timesheet_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/timesheets/{timesheet_id}")

    async def update_timesheet(self, timesheet_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/timesheets/{timesheet_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_timesheet(self, timesheet_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes timesheet retrieval and updates, but not direct deletion."
        )

    async def submit_timesheet(self, timesheet_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/timesheets/{timesheet_id}/submit")

    async def approve_timesheet(self, timesheet_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/timesheets/{timesheet_id}/approve")

    async def reject_timesheet(self, timesheet_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/timesheets/{timesheet_id}/reject")

    async def list_timesheet_entries(self, timesheet_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/timesheets/{timesheet_id}/entries")

    async def create_timesheet_entry(self, timesheet_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/payroll/timesheets/{timesheet_id}/entries",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    # Leave
    async def list_leave_policies(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/leave/policies", params={k: v for k, v in params.items() if v is not None}
        )

    async def create_leave_policy(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/leave/policies", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_leave_policy(self, policy_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/leave/policies/{policy_id}")

    async def update_leave_policy(self, policy_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/leave/policies/{policy_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_leave_policy(self, policy_id: str) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes leave policy retrieval and updates, but not direct deletion."
        )

    async def list_leave_requests(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/leave/requests", params={k: v for k, v in params.items() if v is not None}
        )

    async def create_leave_request(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/leave/requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def approve_leave_request(self, request_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/leave/requests/{request_id}/approve")

    async def reject_leave_request(self, request_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/leave/requests/{request_id}/reject")

    async def update_leave_request(self, request_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/leave/requests/{request_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    # Contractors
    async def list_contractors(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/contractors", params={k: v for k, v in params.items() if v is not None})

    async def create_contractor(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/contractors", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_contractor(self, contractor_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/contractors/{contractor_id}")

    async def update_contractor(self, contractor_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/contractors/{contractor_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_contractor(self, contractor_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/contractors/{contractor_id}")

    async def list_contractor_payments(self, contractor_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/contractors/{contractor_id}/payments")

    async def create_contractor_payment(self, contractor_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/payroll/contractors/{contractor_id}/payments",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def update_contractor_payment(
        self, contractor_id: str, payment_id: str, **kwargs: JSONValue
    ) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/contractors/{contractor_id}/payments/{payment_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def process_contractor_payment(self, contractor_id: str, payment_id: str) -> ResponseValue:
        return await self._client.post(f"/payroll/contractors/{contractor_id}/payments/{payment_id}/process")

    # Deduction Types
    async def list_deduction_types(self) -> ResponseValue:
        return await self._client.get("/payroll/deductions/types")

    async def create_deduction_type(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/deductions/types", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_deduction_type(self, type_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/deductions/types/{type_id}")

    async def update_deduction_type(self, type_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/deductions/types/{type_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_deduction_type(self, type_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/deductions/types/{type_id}")

    # Payslips
    async def list_payslips(self, **params: QueryValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API does not expose a payslip list endpoint; use retrieve_payslip() or employee/"
            "self-service payslip methods."
        )

    async def retrieve_payslip(self, payslip_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/payslips/{payslip_id}")

    async def update_payslip(self, payslip_id: str, **kwargs: JSONValue) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes payslip retrieval, but not direct payslip updates."
        )

    # Shifts
    async def list_shifts(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/shifts", params={k: v for k, v in params.items() if v is not None})

    async def create_shift(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/shifts", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_shift(self, shift_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/shifts/{shift_id}")

    async def update_shift(self, shift_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/shifts/{shift_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_shift(self, shift_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/shifts/{shift_id}")

    # Tax Brackets
    async def list_tax_brackets(self) -> ResponseValue:
        return await self._client.get("/payroll/tax/brackets")

    async def create_tax_bracket(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/tax/brackets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_tax_bracket(self, bracket_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/tax/brackets/{bracket_id}")

    async def update_tax_bracket(self, bracket_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/tax/brackets/{bracket_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_tax_bracket(self, bracket_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/tax/brackets/{bracket_id}")

    # Tax Forms
    async def list_tax_forms(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/tax-forms", params={k: v for k, v in params.items() if v is not None})

    async def generate_tax_forms(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/tax-forms/generate", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_tax_form(self, form_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/tax-forms/{form_id}")

    async def download_tax_form_pdf(self, form_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/tax-forms/{form_id}/pdf", raw_response=True)

    # Compensation
    async def list_compensation_bands(self) -> ResponseValue:
        return await self._client.get("/payroll/compensation/bands")

    async def create_compensation_band(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/compensation/bands", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_compensation_band(self, band_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/compensation/bands/{band_id}")

    async def update_compensation_band(self, band_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/compensation/bands/{band_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def delete_compensation_band(self, band_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/compensation/bands/{band_id}")

    async def list_compensation_reviews(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/compensation/reviews", params={k: v for k, v in params.items() if v is not None}
        )

    async def create_compensation_review(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/compensation/reviews", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_compensation_review(self, review_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/compensation/reviews/{review_id}")

    async def update_compensation_review(self, review_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/compensation/reviews/{review_id}",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def list_compensation_review_entries(self, review_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/compensation/reviews/{review_id}/entries")

    async def create_compensation_review_entry(self, review_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            f"/payroll/compensation/reviews/{review_id}/entries",
            json={_to_camel(k): v for k, v in kwargs.items() if v is not None},
        )

    async def get_equity_analysis(self) -> ResponseValue:
        return await self._client.get("/payroll/compensation/equity-analysis")

    # Approval Chains
    async def list_approval_chains(self) -> ResponseValue:
        return await self._client.get("/payroll/approval-chains")

    async def create_approval_chain(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/approval-chains", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def retrieve_approval_chain(self, chain_id: str) -> ResponseValue:
        return await self._client.get(f"/payroll/approval-chains/{chain_id}")

    async def update_approval_chain(self, chain_id: str, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            f"/payroll/approval-chains/{chain_id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete_approval_chain(self, chain_id: str) -> ResponseValue:
        return await self._client.delete(f"/payroll/approval-chains/{chain_id}")

    # Self-Service
    async def get_self_service_profile(self) -> ResponseValue:
        return await self._client.get("/payroll/self-service/profile")

    async def update_self_service_profile(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            "/payroll/self-service/profile", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def list_self_service_payslips(self) -> ResponseValue:
        return await self._client.get("/payroll/self-service/payslips")

    async def get_self_service_leave_balance(self) -> ResponseValue:
        return await self._client.get("/payroll/self-service/leave-balance")

    async def list_self_service_leave_requests(self) -> ResponseValue:
        raise NotImplementedError(
            "The current v1 API exposes self-service leave request creation, but not listing via this endpoint."
        )

    async def create_self_service_leave_request(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/self-service/leave-requests", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def list_self_service_timesheets(self) -> ResponseValue:
        return await self._client.get("/payroll/self-service/timesheets")

    async def create_self_service_timesheet(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.post(
            "/payroll/self-service/timesheets", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    # Forecasting
    async def get_projection(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/forecasting/projection", params={k: v for k, v in params.items() if v is not None}
        )

    async def get_budget_vs_actual(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/forecasting/budget-vs-actual", params={k: v for k, v in params.items() if v is not None}
        )

    async def get_what_if(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/forecasting/what-if", params={k: v for k, v in params.items() if v is not None}
        )

    # Reports
    async def report_summary(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/reports/summary", params={k: v for k, v in params.items() if v is not None}
        )

    async def report_labor_cost(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/reports/labor-cost", params={k: v for k, v in params.items() if v is not None}
        )

    async def report_tax_liability(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/reports/tax-liability", params={k: v for k, v in params.items() if v is not None}
        )

    async def report_yoy(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get("/payroll/reports/yoy", params={k: v for k, v in params.items() if v is not None})

    async def export_report(self, **params: QueryValue) -> ResponseValue:
        return await self._client.get(
            "/payroll/reports/export", params={k: v for k, v in params.items() if v is not None}
        )

    # Settings
    async def get_settings(self) -> ResponseValue:
        return await self._client.get("/payroll/settings")

    async def update_settings(self, **kwargs: JSONValue) -> ResponseValue:
        return await self._client.patch(
            "/payroll/settings", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )
