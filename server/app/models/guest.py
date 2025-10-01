import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Guest(Base, TimestampMixin):
    __tablename__ = "guests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    couple_id = Column(UUID(as_uuid=True), ForeignKey("couples.id"), nullable=False)

    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    group = Column(String, nullable=True)  # family, friends, colleagues, other

    couple = relationship("Couple", backref="guests")
