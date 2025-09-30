from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID


class CoupleBase(BaseModel):
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    guest_count: Optional[int] = None
    preferred_cities: Optional[List[str]] = None


class CoupleCreate(CoupleBase):
    pass


class CoupleUpdate(CoupleBase):
    pass


class CoupleOut(CoupleBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True
