from __future__ import annotations

import os
from typing import Literal, cast, overload

import httpx

from ._exceptions import (
    APIConnectionError,
    APITimeoutError,
    raise_for_status,
)
from ._types import Body, Headers, JSONValue, QueryParams, ResponseValue
from ._version import __version__

DEFAULT_BASE_URL = "https://dubbl.dev"
DEFAULT_TIMEOUT = 60.0
DEFAULT_MAX_RETRIES = 2


class BaseClient:
    """Shared configuration for sync and async clients."""

    api_key: str
    base_url: str
    organization_id: str | None
    timeout: float
    max_retries: int
    _custom_headers: dict[str, str]

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

    def _build_headers(self, extra: dict[str, str] | None = None) -> dict[str, str]:
        headers: dict[str, str] = {
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
        if path.startswith(("http://", "https://")):
            return path
        if path.startswith("/api/"):
            return f"{self.base_url}{path}"
        if not path.startswith("/"):
            path = f"/{path}"
        return f"{self.base_url}/api/v1{path}"

    def _prepare_params(self, params: QueryParams | None) -> QueryParams | None:
        if params is None:
            return None
        return {k: v for k, v in params.items() if v is not None}


class SyncAPIClient(BaseClient):
    """Synchronous HTTP client."""

    _client: httpx.Client

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
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            organization_id=organization_id,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._client = httpx.Client(timeout=self.timeout)

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        url = self._build_url(path)
        req_headers = self._build_headers(headers)
        clean_params = self._prepare_params(params)

        last_exc: Exception | None = None
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
                body = cast(JSONValue, response.json()) if response.content else None
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

        assert last_exc is not None
        raise last_exc

    @overload
    def get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    def get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    def get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return self.request("GET", path, params=params, headers=headers, raw_response=raw_response)

    @overload
    def post(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    def post(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    def post(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return self.request("POST", path, json=json, params=params, headers=headers, raw_response=raw_response)

    @overload
    def patch(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    def patch(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    def patch(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return self.request("PATCH", path, json=json, params=params, headers=headers, raw_response=raw_response)

    @overload
    def put(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    def put(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    def put(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return self.request("PUT", path, json=json, params=params, headers=headers, raw_response=raw_response)

    @overload
    def delete(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    def delete(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    def delete(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return self.request("DELETE", path, json=json, params=params, headers=headers, raw_response=raw_response)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> SyncAPIClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncAPIClient(BaseClient):
    """Asynchronous HTTP client."""

    _client: httpx.AsyncClient

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
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            organization_id=organization_id,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._client = httpx.AsyncClient(timeout=self.timeout)

    @overload
    async def request(
        self,
        method: str,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    async def request(
        self,
        method: str,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    async def request(
        self,
        method: str,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        url = self._build_url(path)
        req_headers = self._build_headers(headers)
        clean_params = self._prepare_params(params)

        last_exc: Exception | None = None
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
                body = cast(JSONValue, response.json()) if response.content else None
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

        assert last_exc is not None
        raise last_exc

    @overload
    async def get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    async def get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    async def get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return await self.request("GET", path, params=params, headers=headers, raw_response=raw_response)

    @overload
    async def post(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    async def post(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    async def post(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return await self.request("POST", path, json=json, params=params, headers=headers, raw_response=raw_response)

    @overload
    async def patch(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    async def patch(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    async def patch(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return await self.request("PATCH", path, json=json, params=params, headers=headers, raw_response=raw_response)

    @overload
    async def put(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    async def put(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    async def put(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return await self.request("PUT", path, json=json, params=params, headers=headers, raw_response=raw_response)

    @overload
    async def delete(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[True],
    ) -> bytes: ...

    @overload
    async def delete(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: Literal[False] = False,
    ) -> JSONValue: ...

    async def delete(
        self,
        path: str,
        *,
        json: Body | None = None,
        params: QueryParams | None = None,
        headers: Headers | None = None,
        raw_response: bool = False,
    ) -> ResponseValue:
        return await self.request("DELETE", path, json=json, params=params, headers=headers, raw_response=raw_response)

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> AsyncAPIClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
