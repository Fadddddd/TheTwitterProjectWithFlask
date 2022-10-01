"""add customers date_of_birth

Revision ID: 155f8b259aa5
Revises: e719548d863e
Create Date: 2022-09-29 12:42:18.258004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '155f8b259aa5'
down_revision = 'e719548d863e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
