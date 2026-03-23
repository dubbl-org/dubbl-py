from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeAlias, TypeVar

JSONPrimitive: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONPrimitive | dict[str, "JSONValue"] | list["JSONValue"]
JSONObject: TypeAlias = dict[str, JSONValue]
JSONArray: TypeAlias = list[JSONValue]
QueryValue: TypeAlias = JSONValue
QueryParams: TypeAlias = dict[str, QueryValue]
Body: TypeAlias = JSONObject
Headers: TypeAlias = dict[str, str]
ResponseValue: TypeAlias = JSONValue | bytes

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
    params: QueryParams | None = None
