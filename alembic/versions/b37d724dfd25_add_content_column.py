"""add content column

Revision ID: b37d724dfd25
Revises: 62b8b8c5f8b3
Create Date: 2021-12-13 23:30:29.389311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b37d724dfd25'
down_revision = '62b8b8c5f8b3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_orm', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts_orm', 'content')
    pass
