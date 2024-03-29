"""create steam_items table

Revision ID: 8316e819180d
Revises: 
Create Date: 2024-03-29 12:09:15.279485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8316e819180d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'steam_items',
        sa.Column('link', sa.Text, primary_key=True, nullable=False),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('game_id', sa.Integer, nullable=False),
        sa.Column('buy_price', sa.DECIMAL, nullable=False),
        sa.Column('sell_price', sa.DECIMAL, nullable=False),
        sa.Column('buy_orders', sa.Integer, nullable=False),
        sa.Column('sell_orders', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    pass
