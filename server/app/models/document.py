import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Document(Base, TimestampMixin):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    url = Column(String, nullable=False)
    doc_type = Column(String, nullable=True)  # contract, invoice, media, other
    metadata = Column(JSONB, nullable=True)

    owner = relationship("User", backref="documents")
