"""insert dummy data into patients table

Revision ID: 99d6ee248850
Revises: c56289b52385
Create Date: 2025-08-25 12:01:27.793161

"""
from datetime import datetime, date
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '99d6ee248850'
down_revision: Union[str, Sequence[str], None] = 'c56289b52385'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert dummy data into patients table."""
    op.bulk_insert(
        sa.table(
            'patients',
            sa.column('name', sa.String),
            sa.column('surname', sa.String),
            sa.column('date_of_birth', sa.Date),
            sa.column('ingression_date', sa.DateTime),
            sa.column('discharge_date', sa.DateTime),
            sa.column('diagnosis', sa.String),
            sa.column('treatment', sa.String),
            sa.column('notes', sa.Text),
            sa.column('legal_guardian', sa.String),
            sa.column('gender', sa.String),
            sa.column('emergency_contact', sa.String),
            sa.column('created_at', sa.DateTime),
        ),
        [
            {
                'name': 'John',
                'surname': 'Smith',
                'date_of_birth': date(2024, 1, 10),
                'ingression_date': datetime(2025, 8, 20, 10, 0),
                'discharge_date': None,
                'diagnosis': None,
                'treatment': None,
                'notes': None,
                'legal_guardian': 'Anna Smith',
                'gender': 'Male',
                'emergency_contact': '600123456',
                'created_at': datetime.now(),
            },
            {
                'name': 'Lucy',
                'surname': 'Johnson',
                'date_of_birth': date(2024, 2, 15),
                'ingression_date': datetime(2025, 8, 21, 9, 30),
                'discharge_date': None,
                'diagnosis': None,
                'treatment': None,
                'notes': None,
                'legal_guardian': 'Charles Johnson',
                'gender': 'Female',
                'emergency_contact': '600654321',
                'created_at': datetime.now(),
            },
            {
                'name': 'Peter',
                'surname': 'Williams',
                'date_of_birth': date(2024, 3, 5),
                'ingression_date': datetime(2025, 8, 22, 8, 45),
                'discharge_date': None,
                'diagnosis': None,
                'treatment': None,
                'notes': None,
                'legal_guardian': 'Mary Williams',
                'gender': 'Male',
                'emergency_contact': '600987654',
                'created_at': datetime.now(),
            },
        ]
    )


def downgrade() -> None:
    """Delete the inserted dummy data."""
    op.execute("DELETE FROM patients WHERE name IN ('John', 'Lucy', 'Peter')")
