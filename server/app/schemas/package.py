from uuid import UUID

from pydantic import BaseModel


class PackageBase(BaseModel):
    title: str | None = None


class PackageCreate(PackageBase):
    pass


class PackageOut(PackageBase):
    id: UUID
    couple_id: UUID
    status: str
    iteration_count: int
    estimated_total: float | None = None

    class Config:
        from_attributes = True
