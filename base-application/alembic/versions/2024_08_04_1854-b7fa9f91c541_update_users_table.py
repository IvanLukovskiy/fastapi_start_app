"""update users table

Revision ID: b7fa9f91c541
Revises: 95d2a61e77f7
Create Date: 2024-08-04 18:54:54.375595

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b7fa9f91c541"
down_revision: Union[str, None] = "95d2a61e77f7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f("uq_users_foo_bar"), "users", ["foo", "bar"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
