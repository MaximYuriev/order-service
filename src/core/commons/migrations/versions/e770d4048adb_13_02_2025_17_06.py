"""13.02.2025 17:06

Revision ID: e770d4048adb
Revises: 
Create Date: 2025-02-13 17:06:09.830522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e770d4048adb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('order_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('order_price', sa.Integer(), nullable=True),
    sa.Column('order_status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('product_on_order',
    sa.Column('order_id', sa.Uuid(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('quantity_in_order', sa.Integer(), nullable=False),
    sa.Column('price_per_piece', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('order_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_on_order')
    op.drop_table('order')
    # ### end Alembic commands ###
