"""seed_service_categories

Revision ID: 733ea45c5a03
Revises: 4339a3ffd714
Create Date: 2025-10-01 02:16:07.237479

"""
from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '733ea45c5a03'
down_revision: str | Sequence[str] | None = '4339a3ffd714'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Seed common service categories."""
    categories = [
        {"name": "venue", "description": "Venues and banquet halls"},
        {"name": "photography", "description": "Photographers and videographers"},
        {"name": "dj", "description": "DJs and music"},
        {"name": "makeup", "description": "Bridal and party makeup"},
        {"name": "catering", "description": "Caterers and food services"},
        {"name": "decor", "description": "Decorators and florists"},
        {"name": "transport", "description": "Transportation and logistics"},
        {"name": "other", "description": "Other services"},
    ]

    service_categories = sa.table(
        "service_categories",
        sa.column("name", sa.String()),
        sa.column("description", sa.String()),
    )

    op.bulk_insert(service_categories, categories)


def downgrade() -> None:
    """Remove seeded categories."""
    conn = op.get_bind()
    conn.execute(
        sa.text("DELETE FROM service_categories WHERE name IN (:names)"),
        {
            "names": (
                "venue",
                "photography",
                "dj",
                "makeup",
                "catering",
                "decor",
                "transport",
                "other",
            )
        },
    )
