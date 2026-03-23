from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar

T = TypeVar("T")


@dataclass
class PaginatedResponse(Generic[T]):
    """Paginated API response."""

    items: list[T]
    total: int
    page: int
    limit: int
    pages: int


@dataclass
class RequestOptions:
    """Per-request options."""

    timeout: float | None = None
    headers: dict[str, str] | None = None
    params: dict[str, Any] | None = None


QueryParams = Dict[str, Any]
Body = Dict[str, Any]
Headers = Dict[str, str]
