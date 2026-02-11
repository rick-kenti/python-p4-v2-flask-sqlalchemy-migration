"""rename department

Revision ID: 580f32bbf334
Revises: 555d0edc46c8
Create Date: 2026-02-11 17:49:30.592499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '580f32bbf334'
down_revision = '555d0edc46c8'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')

def downgrade():
    op.rename_table('departments', 'department')
