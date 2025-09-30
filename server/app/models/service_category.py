from sqlalchemy import Column, String

from .base import Base


class ServiceCategoryRef(Base):
    __tablename__ = "service_categories"

    # keep it simple: name as primary key
    name = Column(String, primary_key=True)
    description = Column(String, nullable=True)
