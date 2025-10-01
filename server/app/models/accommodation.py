import uuid
from sqlalchemy import Column, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Accommodation(Base, TimestampMixin):
    __tablename__ = "accommodations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    guest_id = Column(UUID(as_uuid=True), ForeignKey("guests.id"), nullable=False)

    hotel_name = Column(String, nullable=True)
    check_in = Column(Date, nullable=True)
    check_out = Column(Date, nullable=True)
    transport_required = Column(Boolean, nullable=True)

    guest = relationship("Guest", backref="accommodation")
