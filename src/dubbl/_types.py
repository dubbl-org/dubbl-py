from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Mapping, Sequence, TypeAlias, TypeVar

JSONPrimitive: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONPrimitive | dict[str, "JSONValue"] | list["JSONValue"]
JSONObject: TypeAlias = dict[str, JSONValue]
JSONArray: TypeAlias = list[JSONValue]
QueryPrimitive: TypeAlias = str | int | float | bool | None
QueryValue: TypeAlias = QueryPrimitive | Sequence[QueryPrimitive]
QueryParams: TypeAlias = Mapping[str, QueryValue]
Body: TypeAlias = Mapping[str, JSONValue]
Headers: TypeAlias = Mapping[str, str]
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
