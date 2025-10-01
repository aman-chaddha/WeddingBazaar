import uuid

from sqlalchemy import JSON, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class FamilyMember(Base, TimestampMixin):
    __tablename__ = "family_members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    couple_id = Column(UUID(as_uuid=True), ForeignKey("couples.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    relation = Column(String, nullable=True)
    permissions = Column(JSON, nullable=True)

    couple = relationship("Couple", backref="family_members")
