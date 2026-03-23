from __future__ import annotations

import httpx

from ._types import ResponseValue


class DubblError(Exception):
    """Base exception for all Dubbl SDK errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class APIError(DubblError):
    """Base exception for API HTTP errors."""

    status_code: int

    response: httpx.Response | None
    body: ResponseValue | None

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response = response
        self.body = body

    def __str__(self) -> str:
        return f"[{self.status_code}] {self.message}"


class AuthenticationError(APIError):
    """401 - Invalid or missing API key."""

    def __init__(
        self,
        message: str = "Invalid or missing API key",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=401, response=response, body=body)


class PermissionDeniedError(APIError):
    """403 - Insufficient permissions."""

    def __init__(
        self,
        message: str = "Permission denied",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=403, response=response, body=body)


class NotFoundError(APIError):
    """404 - Resource not found."""

    def __init__(
        self,
        message: str = "Resource not found",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=404, response=response, body=body)


class ConflictError(APIError):
    """409 - Conflict (duplicate, constraint violation)."""

    def __init__(
        self,
        message: str = "Conflict",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=409, response=response, body=body)


class ValidationError(APIError):
    """400 - Validation error."""

    def __init__(
        self,
        message: str = "Validation error",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=400, response=response, body=body)


class RateLimitError(APIError):
    """429 - Rate limit exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=429, response=response, body=body)


class InternalServerError(APIError):
    """500 - Internal server error."""

    def __init__(
        self,
        message: str = "Internal server error",
        *,
        response: httpx.Response | None = None,
        body: ResponseValue | None = None,
    ) -> None:
        super().__init__(message, status_code=500, response=response, body=body)


class APIConnectionError(DubblError):
    """Network connectivity error."""

    def __init__(self, message: str = "Connection error") -> None:
        super().__init__(message)


class APITimeoutError(APIConnectionError):
    """Request timed out."""

    def __init__(self, message: str = "Request timed out") -> None:
        super().__init__(message)


_STATUS_MAP: dict[int, type[APIError]] = {
    400: ValidationError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    429: RateLimitError,
    500: InternalServerError,
}


def raise_for_status(
    status_code: int,
    body: ResponseValue | None = None,
    response: httpx.Response | None = None,
) -> None:
    """Raise an appropriate exception for an HTTP error status code."""
    if status_code < 400:
        return
    message = "API error"
    if isinstance(body, dict) and "error" in body:
        message = body["error"]
    elif isinstance(body, str):
        message = body
    exc_class = _STATUS_MAP.get(status_code, APIError)
    raise exc_class(message, status_code=status_code, response=response, body=body)
