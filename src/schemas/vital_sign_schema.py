from dataclasses import dataclass
from typing import Optional


@dataclass
class VitalSignSchema:
    patient_id: int
    heart_rate: Optional[int]
    blood_pressure_systolic: Optional[int]
    blood_pressure_diastolic: Optional[int]
    respiratory_rate: Optional[int]
    temperature: Optional[float]
    blood_glucose: Optional[float]
    serum_bilirubin: Optional[float]
    murmurs: Optional[bool]
    abdominal_signs: Optional[bool]
