from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class VendorServiceBase(BaseModel):
    category: str
    title: str
    base_price: Optional[float] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    pricing_unit: Optional[str] = None
    details: Optional[dict] = None


class VendorServiceCreate(VendorServiceBase):
    pass


class VendorServiceOut(VendorServiceBase):
    id: UUID
    vendor_id: UUID

    class Config:
        from_attributes = True
