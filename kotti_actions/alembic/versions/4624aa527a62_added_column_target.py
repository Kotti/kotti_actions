"""Added column target

Revision ID: 4624aa527a62
Revises: None
Create Date: 2015-03-19 12:48:20.336836

"""

# revision identifiers, used by Alembic.
revision = '4624aa527a62'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('link_actions', sa.Column('target', sa.Unicode(30)))


def downgrade():
    op.drop_column('link_actions', 'target')
