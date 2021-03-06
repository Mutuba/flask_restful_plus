"""Add slug

Revision ID: 21c5ad747046
Revises: 6876fcf3d658
Create Date: 2020-12-17 14:03:29.353135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c5ad747046'
down_revision = '6876fcf3d658'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('slug', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'slug')
    # ### end Alembic commands ###
