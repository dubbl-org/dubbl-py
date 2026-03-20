from __future__ import annotations
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class OCR:
    """OCR extraction."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def extract_receipt(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post("/ocr/receipt", json=body)


class AsyncOCR:
    """OCR extraction (async)."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def extract_receipt(self, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post("/ocr/receipt", json=body)
