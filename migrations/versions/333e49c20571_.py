"""empty message

Revision ID: 333e49c20571
Revises: f4cf3e97f574
Create Date: 2017-10-23 01:18:51.847773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333e49c20571'
down_revision = 'f4cf3e97f574'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('password_digest', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
