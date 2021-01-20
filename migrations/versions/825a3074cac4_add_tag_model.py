"""add tag model

Revision ID: 825a3074cac4
Revises: 02d8a84c29d1
Create Date: 2020-12-15 17:05:29.154230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '825a3074cac4'
down_revision = '02d8a84c29d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###
