"""create post table

Revision ID: 62b8b8c5f8b3
Revises: 
Create Date: 2021-12-13 23:27:31.550350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62b8b8c5f8b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts_orm', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts_orm')
    pass
