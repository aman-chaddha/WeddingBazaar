import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Review(Base, TimestampMixin):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"), nullable=False)
    couple_id = Column(UUID(as_uuid=True), ForeignKey("couples.id"), nullable=False)

    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)

    vendor = relationship("Vendor", backref="reviews")
    couple = relationship("Couple", backref="reviews")
