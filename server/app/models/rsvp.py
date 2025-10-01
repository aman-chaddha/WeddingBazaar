import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Rsvp(Base, TimestampMixin):
    __tablename__ = "rsvps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    guest_id = Column(UUID(as_uuid=True), ForeignKey("guests.id"), nullable=False)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), nullable=False)

    response = Column(String, nullable=True)  # yes, no, maybe
    plus_ones = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)

    guest = relationship("Guest", backref="rsvps")
    event = relationship("Event", backref="rsvps")
