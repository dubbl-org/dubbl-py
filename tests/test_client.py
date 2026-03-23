import httpx
import pytest
import respx

from dubbl import AsyncDubbl, Dubbl


class TestClientInit:
    def test_requires_api_key(self) -> None:
        import os

        env_key = os.environ.pop("DUBBL_API_KEY", None)
        try:
            with pytest.raises(ValueError, match="API key must be provided"):
                Dubbl()
        finally:
            if env_key:
                os.environ["DUBBL_API_KEY"] = env_key

    def test_accepts_api_key(self) -> None:
        client = Dubbl(api_key="dk_live_test")
        assert client._client.api_key == "dk_live_test"
        client.close()

    def test_custom_base_url(self) -> None:
        client = Dubbl(api_key="dk_live_test", base_url="https://custom.example.com")
        assert client._client.base_url == "https://custom.example.com"
        client.close()

    def test_has_all_resources(self) -> None:
        client = Dubbl(api_key="dk_live_test")
        assert hasattr(client, "accounts")
        assert hasattr(client, "admin")
        assert hasattr(client, "invoices")
        assert hasattr(client, "entries")
        assert hasattr(client, "bills")
        assert hasattr(client, "contacts")
        assert hasattr(client, "currencies")
        assert hasattr(client, "integrations")
        assert hasattr(client, "payments")
        assert hasattr(client, "reports")
        client.close()

    def test_context_manager(self) -> None:
        with Dubbl(api_key="dk_live_test") as client:
            assert client._client.api_key == "dk_live_test"


class TestAsyncClientInit:
    def test_accepts_api_key(self) -> None:
        client = AsyncDubbl(api_key="dk_live_test")
        assert client._client.api_key == "dk_live_test"

    def test_has_all_resources(self) -> None:
        client = AsyncDubbl(api_key="dk_live_test")
        assert hasattr(client, "accounts")
        assert hasattr(client, "admin")
        assert hasattr(client, "invoices")
        assert hasattr(client, "entries")
        assert hasattr(client, "currencies")
        assert hasattr(client, "integrations")


@respx.mock
def test_sync_resource_paths(client: Dubbl) -> None:
    attachments_route = respx.post("https://test.dubbl.dev/api/v1/attachments/presign").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    admin_route = respx.get("https://test.dubbl.dev/api/v1/admin/users").mock(
        return_value=httpx.Response(200, json={"data": []})
    )
    bank_route = respx.post("https://test.dubbl.dev/api/v1/bank-transactions/txn_123/create-expense").mock(
        return_value=httpx.Response(200, json={"expense": {"id": "exp_123"}})
    )
    portal_route = respx.get("https://test.dubbl.dev/api/portal/token_123").mock(
        return_value=httpx.Response(200, json={"contact": {"id": "contact_123"}})
    )
    report_route = respx.get("https://test.dubbl.dev/api/v1/reports/saved/report_123").mock(
        return_value=httpx.Response(200, json={"report": {"id": "report_123"}})
    )

    assert client.attachments.presign(file_name="invoice.pdf", content_type="application/pdf", file_size=10) == {
        "ok": True
    }
    assert client.admin.list_users() == {"data": []}
    assert client.bank_transactions.create_expense("txn_123", amount=100) == {"expense": {"id": "exp_123"}}
    assert client.portal.get_details("token_123") == {"contact": {"id": "contact_123"}}
    assert client.reports.retrieve_saved("report_123") == {"report": {"id": "report_123"}}

    assert attachments_route.called
    assert admin_route.called
    assert bank_route.called
    assert portal_route.called
    assert report_route.called


@respx.mock
def test_sync_corrected_route_verbs(client: Dubbl) -> None:
    backup_route = respx.get("https://test.dubbl.dev/api/v1/backups/bkp_123/download").mock(
        return_value=httpx.Response(200, content=b'{"backup":true}')
    )
    validation_route = respx.get("https://test.dubbl.dev/api/v1/bank-accounts/ba_123/validate-balance").mock(
        return_value=httpx.Response(200, json={"valid": True})
    )
    payment_link_route = respx.post("https://test.dubbl.dev/api/v1/invoices/inv_123/payment-link").mock(
        return_value=httpx.Response(200, json={"url": "https://pay.example.com"})
    )
    requisition_route = respx.put("https://test.dubbl.dev/api/v1/purchase-requisitions/pr_123").mock(
        return_value=httpx.Response(200, json={"requisition": {"id": "pr_123"}})
    )
    period_lock_route = respx.put("https://test.dubbl.dev/api/v1/period-lock").mock(
        return_value=httpx.Response(200, json={"periodLock": {"lockDate": "2026-03-31"}})
    )

    assert client.backups.download("bkp_123") == b'{"backup":true}'
    assert client.bank_accounts.validate_balance("ba_123") == {"valid": True}
    assert client.invoices.payment_link("inv_123") == {"url": "https://pay.example.com"}
    assert client.purchase_requisitions.update("pr_123", status="approved") == {"requisition": {"id": "pr_123"}}
    assert client.period_lock.lock(lock_date="2026-03-31") == {"periodLock": {"lockDate": "2026-03-31"}}

    assert backup_route.called
    assert validation_route.called
    assert payment_link_route.called
    assert requisition_route.called
    assert period_lock_route.called


def test_stale_endpoints_raise_not_implemented(client: Dubbl) -> None:
    with pytest.raises(NotImplementedError):
        client.approval_requests.update("ar_123", status="approved")
    with pytest.raises(NotImplementedError):
        client.document_emails.send(document_id="doc_123")
    with pytest.raises(NotImplementedError):
        client.inventory.retrieve_category("cat_123")
    with pytest.raises(NotImplementedError):
        client.payroll.list_self_service_leave_requests()


@pytest.mark.asyncio
@respx.mock
async def test_async_resource_paths(async_client: AsyncDubbl) -> None:
    integrations_route = respx.get("https://test.dubbl.dev/api/v1/integrations/stripe/status").mock(
        return_value=httpx.Response(200, json={"connected": True})
    )
    inventory_route = respx.patch("https://test.dubbl.dev/api/v1/inventory/categories/cat_123").mock(
        return_value=httpx.Response(200, json={"category": {"id": "cat_123"}})
    )
    bulk_route = respx.post("https://test.dubbl.dev/api/v1/bulk/bank-transactions/import").mock(
        return_value=httpx.Response(200, json={"jobId": "job_123"})
    )

    assert await async_client.integrations.get_stripe_status() == {"connected": True}
    assert await async_client.inventory.update_category("cat_123", name="Updated") == {"category": {"id": "cat_123"}}
    assert await async_client.bulk.import_bank_transactions(file="statement.csv") == {"jobId": "job_123"}

    assert integrations_route.called
    assert inventory_route.called
    assert bulk_route.called


@pytest.mark.asyncio
@respx.mock
async def test_async_corrected_route_verbs(async_client: AsyncDubbl) -> None:
    role_route = respx.put("https://test.dubbl.dev/api/v1/roles/role_123").mock(
        return_value=httpx.Response(200, json={"role": {"id": "role_123"}})
    )
    mileage_route = respx.put("https://test.dubbl.dev/api/v1/organization/mileage-rate").mock(
        return_value=httpx.Response(200, json={"mileageRate": 72})
    )
    email_config_route = respx.put("https://test.dubbl.dev/api/v1/email-config").mock(
        return_value=httpx.Response(200, json={"config": {"provider": "smtp"}})
    )

    assert await async_client.roles.update("role_123", name="Controller") == {"role": {"id": "role_123"}}
    assert await async_client.organization.update_mileage_rate(mileage_rate=72) == {"mileageRate": 72}
    assert await async_client.email_config.update(provider="smtp") == {"config": {"provider": "smtp"}}

    assert role_route.called
    assert mileage_route.called
    assert email_config_route.called
