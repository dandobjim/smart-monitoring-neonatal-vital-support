"""create materialised view of vital_sign without duplications

Revision ID: b7dc9ef02381
Revises: 99d6ee248850
Create Date: 2025-08-28 10:35:39.384377

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b7dc9ef02381'
down_revision: Union[str, Sequence[str], None] = '99d6ee248850'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        CREATE MATERIALIZED VIEW IF NOT EXISTS vital_sign_mv AS
        SELECT DISTINCT ON (patient_id, timestamp)
            id,
            patient_id,
            timestamp,
            heart_rate,
            blood_pressure_systolic,
            blood_pressure_diastolic,
            respiratory_rate,
            temperature,
            blood_glucose,
            serum_bilirubin,
            murmurs,
            abdominal_signs
        FROM vital_signs
        ORDER BY patient_id, timestamp, id;

        -- Create an index to optimize queries on the materialized view
        CREATE INDEX IF NOT EXISTS idx_vital_sign_mv_patient_timestamp ON vital_sign_mv (patient_id, timestamp);

    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP MATERIALIZED VIEW IF EXISTS vital_sign_mv;")
