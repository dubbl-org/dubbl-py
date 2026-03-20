from __future__ import annotations
from typing import Any, Optional


class DubblError(Exception):
    """Base exception for all Dubbl SDK errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class APIError(DubblError):
    """Base exception for API HTTP errors."""
    status_code: int

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        response: Any = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response = response
        self.body = body

    def __str__(self) -> str:
        return f"[{self.status_code}] {self.message}"


class AuthenticationError(APIError):
    """401 - Invalid or missing API key."""
    def __init__(self, message: str = "Invalid or missing API key", **kwargs: Any) -> None:
        super().__init__(message, status_code=401, **kwargs)


class PermissionDeniedError(APIError):
    """403 - Insufficient permissions."""
    def __init__(self, message: str = "Permission denied", **kwargs: Any) -> None:
        super().__init__(message, status_code=403, **kwargs)


class NotFoundError(APIError):
    """404 - Resource not found."""
    def __init__(self, message: str = "Resource not found", **kwargs: Any) -> None:
        super().__init__(message, status_code=404, **kwargs)


class ConflictError(APIError):
    """409 - Conflict (duplicate, constraint violation)."""
    def __init__(self, message: str = "Conflict", **kwargs: Any) -> None:
        super().__init__(message, status_code=409, **kwargs)


class ValidationError(APIError):
    """400 - Validation error."""
    def __init__(self, message: str = "Validation error", **kwargs: Any) -> None:
        super().__init__(message, status_code=400, **kwargs)


class RateLimitError(APIError):
    """429 - Rate limit exceeded."""
    def __init__(self, message: str = "Rate limit exceeded", **kwargs: Any) -> None:
        super().__init__(message, status_code=429, **kwargs)


class InternalServerError(APIError):
    """500 - Internal server error."""
    def __init__(self, message: str = "Internal server error", **kwargs: Any) -> None:
        super().__init__(message, status_code=500, **kwargs)


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


def raise_for_status(status_code: int, body: Any = None, response: Any = None) -> None:
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
