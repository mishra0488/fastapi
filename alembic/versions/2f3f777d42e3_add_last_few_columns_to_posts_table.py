"""add last few columns to posts table

Revision ID: 2f3f777d42e3
Revises: a9f51ec3f2fe
Create Date: 2021-12-13 23:38:20.475406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f3f777d42e3'
down_revision = 'a9f51ec3f2fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_orm', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts_orm', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts_orm', 'published')
    op.drop_column('posts_orm', 'created_at')
    pass
