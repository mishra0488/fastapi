"""create post table

Revision ID: e9775e11d3fa
Revises: 
Create Date: 2021-12-12 23:11:46.133892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9775e11d3fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts_alembic', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts_alembic')
    pass
