import pytest
from dubbl import Dubbl, AsyncDubbl


@pytest.fixture
def api_key() -> str:
    return "dk_live_test_key_for_testing_12345678"


@pytest.fixture
def client(api_key: str) -> Dubbl:
    with Dubbl(api_key=api_key, base_url="https://test.dubbl.dev") as client:
        yield client


@pytest.fixture
async def async_client(api_key: str) -> AsyncDubbl:
    async with AsyncDubbl(api_key=api_key, base_url="https://test.dubbl.dev") as client:
        yield client
