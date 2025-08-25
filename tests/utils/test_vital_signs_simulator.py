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
    assert 60 <= vital_sign.heart_rate <= 100
    assert 90 <= vital_sign.blood_pressure_systolic <= 120
    assert 60 <= vital_sign.blood_pressure_diastolic <= 80
    assert 12 <= vital_sign.respiratory_rate <= 20
    assert 36.1 <= vital_sign.temperature <= 37.2
    assert 70.0 <= vital_sign.blood_glucose <= 140.0
    assert 0.1 <= vital_sign.serum_bilirubin <= 1.2
    assert isinstance(vital_sign.murmurs, bool)
    assert isinstance(vital_sign.abdominal_signs, bool)
