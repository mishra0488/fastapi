"""add users table

Revision ID: 988479e17ef7
Revises: b37d724dfd25
Create Date: 2021-12-13 23:32:50.430400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '988479e17ef7'
down_revision = 'b37d724dfd25'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
