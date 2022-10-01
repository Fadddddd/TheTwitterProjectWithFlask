"""create customers

Revision ID: e719548d863e
Revises: 
Create Date: 2022-09-29 12:39:19.916618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e719548d863e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )

def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
