import uuid
from sqlalchemy import Column, String, ForeignKey, Numeric, Date, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin
from .common_enums import BookingStatus, PaymentStatus, PaymentMethod


class Booking(Base, TimestampMixin):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    couple_id = Column(UUID(as_uuid=True), ForeignKey("couples.id"), nullable=False)
    package_id = Column(UUID(as_uuid=True), ForeignKey("packages.id"), nullable=False)

    status = Column(BookingStatus, nullable=False, default="pending")
    event_date = Column(Date, nullable=True)
    venue_address = Column(String, nullable=True)
    total_amount = Column(Numeric, nullable=True)

    payments = relationship("Payment", back_populates="booking", cascade="all, delete-orphan")
    events = relationship("Event", back_populates="booking", cascade="all, delete-orphan")


class Payment(Base, TimestampMixin):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_id = Column(UUID(as_uuid=True), ForeignKey("bookings.id"), nullable=False)
    amount = Column(Numeric, nullable=False)
    currency = Column(String, nullable=False, default="INR")
    status = Column(PaymentStatus, nullable=False, default="pending")
    method = Column(PaymentMethod, nullable=True)
    escrow_hold = Column(Boolean, nullable=False, default=False)
    stripe_payment_intent_id = Column(String, nullable=True)

    booking = relationship("Booking", back_populates="payments")
    transactions = relationship("PaymentTransaction", back_populates="payment", cascade="all, delete-orphan")


class PaymentTransaction(Base, TimestampMixin):
    __tablename__ = "payment_transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.id"), nullable=False)
    type = Column(String, nullable=False)  # authorize, capture, refund
    amount = Column(Numeric, nullable=False)
    stripe_charge_id = Column(String, nullable=True)
    status = Column(String, nullable=False, default="success")

    payment = relationship("Payment", back_populates="transactions")
