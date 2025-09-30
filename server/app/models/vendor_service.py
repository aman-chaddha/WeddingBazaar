import uuid
from sqlalchemy import Column, String, ForeignKey, Numeric, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin
from .common_enums import ServiceCategory


class VendorService(Base, TimestampMixin):
    __tablename__ = "vendor_services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"), nullable=False)

    category = Column(ServiceCategory, nullable=False)
    title = Column(String, nullable=False)

    base_price = Column(Numeric, nullable=True)
    min_price = Column(Numeric, nullable=True)
    max_price = Column(Numeric, nullable=True)
    pricing_unit = Column(String, nullable=True)  # per_day, per_event, per_guest
    details = Column(JSON, nullable=True)

    vendor = relationship("Vendor", back_populates="services")
