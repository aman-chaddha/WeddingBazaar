import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin
from .common_enums import TaskStatus


class Event(Base, TimestampMixin):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_id = Column(UUID(as_uuid=True), ForeignKey("bookings.id"), nullable=False)
    name = Column(String, nullable=False)  # Mehendi, Sangeet, Wedding, Reception
    start_at = Column(DateTime(timezone=True), nullable=True)
    end_at = Column(DateTime(timezone=True), nullable=True)
    location = Column(String, nullable=True)

    booking = relationship("Booking", back_populates="events")
    tasks = relationship("EventTask", back_populates="event", cascade="all, delete-orphan")


class EventTask(Base, TimestampMixin):
    __tablename__ = "event_tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), nullable=False)
    title = Column(String, nullable=False)
    assigned_vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"), nullable=True)
    status = Column(TaskStatus, nullable=False, default="todo")
    due_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    event = relationship("Event", back_populates="tasks")
