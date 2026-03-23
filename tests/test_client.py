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
