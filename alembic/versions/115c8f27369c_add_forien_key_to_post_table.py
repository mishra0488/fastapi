"""add forien key to post table

Revision ID: 115c8f27369c
Revises: a5b9e9676450
Create Date: 2021-12-12 23:37:35.749222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115c8f27369c'
down_revision = 'a5b9e9676450'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_alembic', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts_alembic", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts_alembic")
    op.drop_column('posts_alembic', 'owner_id')
    pass
