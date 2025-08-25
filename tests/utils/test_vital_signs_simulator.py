import pytest

from src.schemas.vital_sign_schema import VitalSignSchema
from src.utils.vital_signs_simulator import VitalSignsSimulator, PATIENTS


@pytest.fixture
def simulator():
    return VitalSignsSimulator()


def test_simulate_vital_signs_returns_valid_schema(simulator):
    vital_sign = simulator.simulate_vital_signs()

    assert isinstance(vital_sign, VitalSignSchema)
    assert vital_sign.patient_id in PATIENTS
    assert 60 <= vital_sign.heart_rate <= 190
    assert 50 <= vital_sign.blood_pressure_systolic <= 90
    assert 30 <= vital_sign.blood_pressure_diastolic <= 60
    assert 12 <= vital_sign.respiratory_rate <= 70
    assert 36.1 <= vital_sign.temperature <= 38.2
    assert 40.0 <= vital_sign.blood_glucose <= 140.0
    assert 4.0 <= vital_sign.serum_bilirubin <= 16.0
    assert isinstance(vital_sign.murmurs, bool)
    assert isinstance(vital_sign.abdominal_signs, bool)
