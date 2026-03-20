from __future__ import annotations
from typing import Any, Dict, List, Optional, TypeVar, Generic
from dataclasses import dataclass, field


T = TypeVar("T")


@dataclass
class PaginatedResponse(Generic[T]):
    """Paginated API response."""
    items: List[T]
    total: int
    page: int
    limit: int
    pages: int


@dataclass
class RequestOptions:
    """Per-request options."""
    timeout: Optional[float] = None
    headers: Optional[Dict[str, str]] = None
    params: Optional[Dict[str, Any]] = None


QueryParams = Dict[str, Any]
Body = Dict[str, Any]
Headers = Dict[str, str]
