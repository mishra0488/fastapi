"""add foriegn key to post table

Revision ID: a9f51ec3f2fe
Revises: 988479e17ef7
Create Date: 2021-12-13 23:34:56.469787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9f51ec3f2fe'
down_revision = '988479e17ef7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_orm', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_orm_users_fk', source_table="posts_orm", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_orm_users_fk', table_name="posts_orm")
    op.drop_column('posts_orm', 'owner_id')
    pass
