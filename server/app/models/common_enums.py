from sqlalchemy import Enum

# Enumerations used across the schema

ServiceCategory = Enum(
    "venue",
    "photography",
    "dj",
    "makeup",
    "catering",
    "decor",
    "transport",
    "other",
    name="service_category",
)

PackageStatus = Enum(
    "draft",
    "proposed",
    "iterating",
    "accepted",
    "booked",
    name="package_status",
)

ItemStatus = Enum(
    "suggested",
    "accepted",
    "replaced",
    "removed",
    name="item_status",
)

BookingStatus = Enum(
    "pending",
    "confirmed",
    "in_progress",
    "completed",
    "cancelled",
    name="booking_status",
)

PaymentStatus = Enum(
    "pending",
    "authorized",
    "captured",
    "refunded",
    "failed",
    name="payment_status",
)

PaymentMethod = Enum(
    "card",
    "upi",
    "netbanking",
    "other",
    name="payment_method",
)

TaskStatus = Enum(
    "todo",
    "in_progress",
    "done",
    name="task_status",
)
