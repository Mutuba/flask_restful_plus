"""empty message

Revision ID: ed5ba7dbdc90
Revises: d001efc3dd06
Create Date: 2020-11-30 14:12:57.135390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed5ba7dbdc90'
down_revision = 'd001efc3dd06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('rbac_role_permission_map',
    sa.Column('role_pkey', sa.Integer(), nullable=True),
    sa.Column('permission_pkey', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission_pkey'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['role_pkey'], ['roles.id'], )
    )
    op.create_table('rbac_user_role_map',
    sa.Column('user_pkey', sa.Integer(), nullable=True),
    sa.Column('role_pkey', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_pkey'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_pkey'], ['user.id'], )
    )
    op.add_column('user', sa.Column('_pwhash', sa.String(length=511), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', '_pwhash')
    op.drop_table('rbac_user_role_map')
    op.drop_table('rbac_role_permission_map')
    op.drop_table('roles')
    op.drop_table('permissions')
    # ### end Alembic commands ###
