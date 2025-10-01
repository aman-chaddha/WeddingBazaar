import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class SeatingTable(Base, TimestampMixin):
    __tablename__ = "seating_tables"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), nullable=False)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=True)

    event = relationship("Event", backref="seating_tables")


class SeatingAssignment(Base, TimestampMixin):
    __tablename__ = "seating_assignments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seating_table_id = Column(UUID(as_uuid=True), ForeignKey("seating_tables.id"), nullable=False)
    guest_id = Column(UUID(as_uuid=True), ForeignKey("guests.id"), nullable=False)

    seating_table = relationship("SeatingTable", backref="assignments")
    guest = relationship("Guest", backref="seating_assignment")
