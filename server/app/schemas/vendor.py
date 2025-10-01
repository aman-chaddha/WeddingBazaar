from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class VendorBase(BaseModel):
    business_name: str
    description: str | None = None
    city: str | None = None


class VendorCreate(VendorBase):
    pass


class VendorUpdate(BaseModel):
    business_name: str | None = None
    description: str | None = None
    city: str | None = None


class VendorOut(VendorBase):
    id: UUID
    user_id: UUID
    rating_avg: float | None = None
    review_count: int | None = None
    verified: bool = False

    class Config:
        from_attributes = True
