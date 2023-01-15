"""add last few columns to posts table

Revision ID: d34d2e776157
Revises: 068b3ae79bfa
Create Date: 2023-01-15 14:52:41.913156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd34d2e776157'
down_revision = '068b3ae79bfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, 
        server_default=sa.text('NOW()')
    ))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
