import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class VendorStatusUpdate(Base, TimestampMixin):
    __tablename__ = "vendor_status_updates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), nullable=False)
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"), nullable=False)

    message = Column(String, nullable=True)
    status = Column(String, nullable=True)  # en_route, setup_in_progress, setup_complete, service_delivered

    event = relationship("Event", backref="status_updates")
    vendor = relationship("Vendor")
