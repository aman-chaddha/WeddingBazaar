from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID


class PackageBase(BaseModel):
    title: Optional[str] = None


class PackageCreate(PackageBase):
    pass


class PackageOut(PackageBase):
    id: UUID
    couple_id: UUID
    status: str
    iteration_count: int
    estimated_total: Optional[float] = None

    class Config:
        from_attributes = True
