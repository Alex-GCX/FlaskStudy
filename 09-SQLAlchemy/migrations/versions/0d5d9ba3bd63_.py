"""empty message

Revision ID: 0d5d9ba3bd63
Revises: b9fb2cb382a2
Create Date: 2020-08-07 13:20:39.312148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d5d9ba3bd63'
down_revision = 'b9fb2cb382a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('test_users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'test_users', 'test_roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'test_users', type_='foreignkey')
    op.drop_column('test_users', 'role_id')
    op.drop_table('test_roles')
    # ### end Alembic commands ###
