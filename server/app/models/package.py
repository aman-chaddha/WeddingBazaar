import uuid

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin
from .common_enums import ItemStatus, PackageStatus


class Package(Base, TimestampMixin):
    __tablename__ = "packages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    couple_id = Column(UUID(as_uuid=True), ForeignKey("couples.id"), nullable=False)
    title = Column(String, nullable=True)
    status = Column(PackageStatus, nullable=False, default="draft")
    iteration_count = Column(Integer, nullable=False, default=0)
    estimated_total = Column(Numeric, nullable=True)

    couple = relationship("Couple", back_populates="packages")
    items = relationship(
        "PackageItem",
        back_populates="package",
        cascade="all, delete-orphan",
    )


class PackageItem(Base, TimestampMixin):
    __tablename__ = "package_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    package_id = Column(UUID(as_uuid=True), ForeignKey("packages.id"), nullable=False)
    vendor_service_id = Column(UUID(as_uuid=True), ForeignKey("vendor_services.id"), nullable=True)

    category = Column(String, nullable=True)  # mirror vendor_services.category text for flexibility
    description = Column(String, nullable=True)
    estimated_cost = Column(Numeric, nullable=True)
    final_cost = Column(Numeric, nullable=True)
    status = Column(ItemStatus, nullable=False, default="suggested")

    package = relationship("Package", back_populates="items")
    shortlists = relationship(
        "VendorShortlist",
        back_populates="package_item",
        cascade="all, delete-orphan",
    )


class VendorShortlist(Base, TimestampMixin):
    __tablename__ = "vendor_shortlists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    package_item_id = Column(UUID(as_uuid=True), ForeignKey("package_items.id"), nullable=False)
    vendor_service_id = Column(UUID(as_uuid=True), ForeignKey("vendor_services.id"), nullable=False)
    rank = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)

    package_item = relationship("PackageItem", back_populates="shortlists")
