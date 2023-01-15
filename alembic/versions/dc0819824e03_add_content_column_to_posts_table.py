"""add content column to posts table

Revision ID: dc0819824e03
Revises: dd69c0cd60ba
Create Date: 2023-01-15 13:09:21.597601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0819824e03'
down_revision = 'dd69c0cd60ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
