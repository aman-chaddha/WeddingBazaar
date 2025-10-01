from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class VendorServiceBase(BaseModel):
    category: str
    title: str
    base_price: float | None = None
    min_price: float | None = None
    max_price: float | None = None
    pricing_unit: str | None = None
    details: dict | None = None


class VendorServiceCreate(VendorServiceBase):
    pass


class VendorServiceOut(VendorServiceBase):
    id: UUID
    vendor_id: UUID

    class Config:
        from_attributes = True
