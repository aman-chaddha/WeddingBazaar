import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Message(Base, TimestampMixin):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sender_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    receiver_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    package_item_id = Column(UUID(as_uuid=True), ForeignKey("package_items.id"), nullable=True)

    body = Column(String, nullable=False)
    read_at = Column(DateTime(timezone=True), nullable=True)

    sender = relationship("User", foreign_keys=[sender_user_id])
    receiver = relationship("User", foreign_keys=[receiver_user_id])
