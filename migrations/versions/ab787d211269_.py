"""empty message

Revision ID: ab787d211269
Revises: ed5ba7dbdc90
Create Date: 2020-11-30 20:30:12.223568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab787d211269'
down_revision = 'ed5ba7dbdc90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('boss_name', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('engineer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('engineer_name', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('engineer')
    op.drop_table('boss')
    op.drop_table('employee')
    # ### end Alembic commands ###