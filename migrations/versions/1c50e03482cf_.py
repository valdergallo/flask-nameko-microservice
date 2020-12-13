"""empty message

Revision ID: 1c50e03482cf
Revises: 
Create Date: 2020-12-12 19:46:38.222550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c50e03482cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('code', sa.String(length=200), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('assignee', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_code'), 'inventory', ['code'], unique=False)
    op.create_index(op.f('ix_inventory_type'), 'inventory', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_type'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_code'), table_name='inventory')
    op.drop_table('inventory')
    # ### end Alembic commands ###
