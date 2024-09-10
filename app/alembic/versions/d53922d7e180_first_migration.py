"""First migration

Revision ID: d53922d7e180
Revises: ce700affcbaf
Create Date: 2023-11-24 17:02:57.776362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd53922d7e180'
down_revision: Union[str, None] = 'ce700affcbaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
