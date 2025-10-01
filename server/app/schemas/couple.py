from uuid import UUID

from pydantic import BaseModel


class CoupleBase(BaseModel):
    budget_min: float | None = None
    budget_max: float | None = None
    guest_count: int | None = None
    preferred_cities: list[str] | None = None


class CoupleCreate(CoupleBase):
    pass


class CoupleUpdate(CoupleBase):
    pass


class CoupleOut(CoupleBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True
