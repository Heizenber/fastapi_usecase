"""add user table

Revision ID: 0b40ec988a1c
Revises: dc0819824e03
Create Date: 2023-01-15 13:15:47.062287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b40ec988a1c'
down_revision = 'dc0819824e03'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('email', sa.String(), nullable=False),
                sa.Column('password', sa.String(), nullable=False),
                sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                        server_default=sa.text('now()'), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
