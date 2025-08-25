"""create patients table

Revision ID: 90964fb94286
Revises:
Create Date: 2025-08-25 11:41:49.653358

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '90964fb94286'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('patients',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('surname', sa.String(length=100), nullable=False),
                    sa.Column('date_of_birth', sa.Date(), nullable=False),
                    sa.Column('ingression_date', sa.DateTime(), nullable=False),
                    sa.Column('discharge_date', sa.DateTime(), nullable=True),
                    sa.Column('diagnosis', sa.String(length=255), nullable=True),
                    sa.Column('treatment', sa.String(length=255), nullable=True),
                    sa.Column('notes', sa.Text(), nullable=True),
                    sa.Column('legal_guardian', sa.String(length=100), nullable=True),
                    sa.Column('gender', sa.String(length=100), nullable=True),
                    sa.Column('emergency_contact', sa.String(length=100), nullable=True),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False, index=True,
                              default=sa.func.now()),
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('patients')
