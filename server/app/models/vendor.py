import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Vendor(Base, TimestampMixin):
    __tablename__ = "vendors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)

    business_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    city = Column(String, nullable=True)

    rating_avg = Column(Numeric, nullable=True)
    review_count = Column(Numeric, nullable=True)
    verified = Column(Boolean, nullable=False, default=False)

    user = relationship("User", backref="vendor", uselist=False)
    services = relationship("VendorService", back_populates="vendor")
