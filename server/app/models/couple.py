import uuid

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Couple(Base, TimestampMixin):
    __tablename__ = "couples"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    budget_min = Column(Numeric, nullable=True)
    budget_max = Column(Numeric, nullable=True)
    guest_count = Column(Integer, nullable=True)
    preferred_cities = Column(ARRAY(String), nullable=True)
    # For simplicity, dates can be handled in a separate table later

    user = relationship("User", backref="couple", uselist=False)
    packages = relationship("Package", back_populates="couple")
