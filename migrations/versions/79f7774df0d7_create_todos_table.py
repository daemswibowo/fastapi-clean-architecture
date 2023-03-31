"""create todos table

Revision ID: 79f7774df0d7
Revises:
Create Date: 2023-03-02 17:19:08.118283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "79f7774df0d7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "todos",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("title", sa.Text, nullable=False),
        sa.Column("is_done", sa.Boolean, nullable=False, default=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            default=sa.func.now(),
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True)),
    )


def downgrade() -> None:
    op.drop_table("todos")
