"""Renaming students to scholars

Revision ID: f8b246ab67fe
Revises: 791279dd0760
Create Date: 2023-06-04 12:30:43.316163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b246ab67fe'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    


def downgrade() -> None:
    op.rename_table('scholars', 'students')
