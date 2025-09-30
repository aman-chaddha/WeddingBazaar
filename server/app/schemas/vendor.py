from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class VendorBase(BaseModel):
    business_name: str
    description: Optional[str] = None
    city: Optional[str] = None


class VendorCreate(VendorBase):
    pass


class VendorUpdate(BaseModel):
    business_name: Optional[str] = None
    description: Optional[str] = None
    city: Optional[str] = None


class VendorOut(VendorBase):
    id: UUID
    user_id: UUID
    rating_avg: Optional[float] = None
    review_count: Optional[int] = None
    verified: bool = False

    class Config:
        from_attributes = True
