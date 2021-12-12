"""add few last columns in posts table

Revision ID: d628c8e7b7d3
Revises: 115c8f27369c
Create Date: 2021-12-12 23:53:43.434126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd628c8e7b7d3'
down_revision = '115c8f27369c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_alembic', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts_alembic', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts_alembic', 'published')
    op.drop_column('posts_alembic', 'created_at')
    pass
