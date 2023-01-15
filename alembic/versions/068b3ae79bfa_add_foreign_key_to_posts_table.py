"""add foreign-key to posts table

Revision ID: 068b3ae79bfa
Revises: 0b40ec988a1c
Create Date: 2023-01-15 13:24:28.982178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '068b3ae79bfa'
down_revision = '0b40ec988a1c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', 
    referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
