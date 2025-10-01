import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class ServiceMedia(Base, TimestampMixin):
    __tablename__ = "service_media"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vendor_service_id = Column(UUID(as_uuid=True), ForeignKey("vendor_services.id"), nullable=False)

    url = Column(String, nullable=False)
    media_type = Column(String, nullable=True)  # image, video
    caption = Column(String, nullable=True)

    vendor_service = relationship("VendorService", backref="media")
