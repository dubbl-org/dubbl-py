import pytest
from dubbl import Dubbl, AsyncDubbl, DubblError


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
        assert hasattr(client, "invoices")
        assert hasattr(client, "entries")
        assert hasattr(client, "bills")
        assert hasattr(client, "contacts")
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
        assert hasattr(client, "invoices")
        assert hasattr(client, "entries")
