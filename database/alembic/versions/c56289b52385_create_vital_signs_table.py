"""create vital_signs table

Revision ID: c56289b52385
Revises: 90964fb94286
Create Date: 2025-08-25 11:50:10.582428

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c56289b52385'
down_revision: Union[str, Sequence[str], None] = '90964fb94286'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('vital_signs',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('patient_id', sa.Integer(), sa.ForeignKey('patients.id'), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=False, server_default=sa.func.now()),
                    sa.Column('heart_rate', sa.Integer(), nullable=True),
                    sa.Column('blood_pressure_systolic', sa.Integer(), nullable=True),
                    sa.Column('blood_pressure_diastolic', sa.Integer(), nullable=True),
                    sa.Column('respiratory_rate', sa.Integer(), nullable=True),
                    sa.Column('temperature', sa.Float(), nullable=True),
                    sa.Column('blood_glucose', sa.Float(), nullable=True),
                    sa.Column('serum_bilirubin', sa.Float(), nullable=True),
                    sa.Column('murmurs', sa.Boolean(), nullable=True),
                    sa.Column('abdominal_signs', sa.Boolean(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('vital_signs')
