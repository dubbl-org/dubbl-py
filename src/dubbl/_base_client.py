from __future__ import annotations

import os
from typing import Any, Dict, Optional, Union
from urllib.parse import urljoin

import httpx

from ._exceptions import (
    APIConnectionError,
    APITimeoutError,
    raise_for_status,
)
from ._types import Body, Headers, QueryParams
from ._version import __version__

DEFAULT_BASE_URL = "https://app.dubbl.dev"
DEFAULT_TIMEOUT = 60.0
DEFAULT_MAX_RETRIES = 2


class BaseClient:
    """Shared configuration for sync and async clients."""

    api_key: str
    base_url: str
    organization_id: Optional[str]
    timeout: float
    max_retries: int
    _custom_headers: Dict[str, str]

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
        self.api_key = api_key or os.environ.get("DUBBL_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "The API key must be provided either as the 'api_key' argument "
                "or via the DUBBL_API_KEY environment variable."
            )
        self.base_url = (base_url or os.environ.get("DUBBL_BASE_URL", DEFAULT_BASE_URL)).rstrip("/")
        self.organization_id = organization_id or os.environ.get("DUBBL_ORGANIZATION_ID")
        self.timeout = timeout if timeout is not None else DEFAULT_TIMEOUT
        self.max_retries = max_retries if max_retries is not None else DEFAULT_MAX_RETRIES
        self._custom_headers = default_headers or {}

    def _build_headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": f"dubbl-python/{__version__}",
        }
        if self.organization_id:
            headers["x-organization-id"] = self.organization_id
        headers.update(self._custom_headers)
        if extra:
            headers.update(extra)
        return headers

    def _build_url(self, path: str) -> str:
        if not path.startswith("/"):
            path = f"/{path}"
        return f"{self.base_url}/api/v1{path}"

    def _prepare_params(self, params: Optional[QueryParams]) -> Optional[QueryParams]:
        if params is None:
            return None
        return {k: v for k, v in params.items() if v is not None}


class SyncAPIClient(BaseClient):
    """Synchronous HTTP client."""

    _client: httpx.Client

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._client = httpx.Client(timeout=self.timeout)

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Optional[Body] = None,
        params: Optional[QueryParams] = None,
        headers: Optional[Headers] = None,
        raw_response: bool = False,
    ) -> Any:
        url = self._build_url(path)
        req_headers = self._build_headers(headers)
        clean_params = self._prepare_params(params)

        last_exc: Optional[Exception] = None
        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    url,
                    json=json,
                    params=clean_params,
                    headers=req_headers,
                )
                if raw_response:
                    response.raise_for_status()
                    return response.content
                body = response.json() if response.content else None
                raise_for_status(response.status_code, body=body, response=response)
                return body
            except httpx.TimeoutException as e:
                last_exc = APITimeoutError(str(e))
                if attempt == self.max_retries:
                    raise last_exc from e
            except httpx.ConnectError as e:
                last_exc = APIConnectionError(str(e))
                if attempt == self.max_retries:
                    raise last_exc from e

        raise last_exc  # type: ignore[misc]

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Any:
        return self.request("POST", path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> Any:
        return self.request("PATCH", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Any:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Any:
        return self.request("DELETE", path, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> SyncAPIClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


class AsyncAPIClient(BaseClient):
    """Asynchronous HTTP client."""

    _client: httpx.AsyncClient

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._client = httpx.AsyncClient(timeout=self.timeout)

    async def request(
        self,
        method: str,
        path: str,
        *,
        json: Optional[Body] = None,
        params: Optional[QueryParams] = None,
        headers: Optional[Headers] = None,
        raw_response: bool = False,
    ) -> Any:
        url = self._build_url(path)
        req_headers = self._build_headers(headers)
        clean_params = self._prepare_params(params)

        last_exc: Optional[Exception] = None
        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    url,
                    json=json,
                    params=clean_params,
                    headers=req_headers,
                )
                if raw_response:
                    response.raise_for_status()
                    return response.content
                body = response.json() if response.content else None
                raise_for_status(response.status_code, body=body, response=response)
                return body
            except httpx.TimeoutException as e:
                last_exc = APITimeoutError(str(e))
                if attempt == self.max_retries:
                    raise last_exc from e
            except httpx.ConnectError as e:
                last_exc = APIConnectionError(str(e))
                if attempt == self.max_retries:
                    raise last_exc from e

        raise last_exc  # type: ignore[misc]

    async def get(self, path: str, **kwargs: Any) -> Any:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> Any:
        return await self.request("POST", path, **kwargs)

    async def patch(self, path: str, **kwargs: Any) -> Any:
        return await self.request("PATCH", path, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> Any:
        return await self.request("PUT", path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> Any:
        return await self.request("DELETE", path, **kwargs)

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> AsyncAPIClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
