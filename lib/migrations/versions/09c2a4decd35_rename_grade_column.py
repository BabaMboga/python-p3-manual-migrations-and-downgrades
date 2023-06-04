"""Rename grade column

Revision ID: 09c2a4decd35
Revises: f8b246ab67fe
Create Date: 2023-06-04 13:01:20.588599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c2a4decd35'
down_revision = 'f8b246ab67fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('grade', 'class_grade')


def downgrade() -> None:
    op.alter_column('class_grade', 'grade')
