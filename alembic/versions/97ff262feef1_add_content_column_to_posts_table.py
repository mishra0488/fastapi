"""add content column to posts table

Revision ID: 97ff262feef1
Revises: d628c8e7b7d3
Create Date: 2021-12-12 23:59:57.215908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97ff262feef1'
down_revision = 'd628c8e7b7d3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_alembic', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts_alembic', 'content')
    pass
