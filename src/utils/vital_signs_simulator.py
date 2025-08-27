import random
import time

from faker import Faker

from src.schemas.vital_sign_schema import VitalSignSchema

PATIENTS = [1, 2, 3]


class VitalSignsSimulator:
    def __init__(self):
        self.fake = Faker()

    def simulate_vital_signs(self) -> VitalSignSchema:
        return VitalSignSchema(
            patient_id=self.fake.random_element(elements=PATIENTS),
            heart_rate=self.fake.random_int(min=60, max=190),
            blood_pressure_systolic=self.fake.random_int(min=50, max=90),
            blood_pressure_diastolic=self.fake.random_int(min=30, max=60),
            respiratory_rate=self.fake.random_int(min=12, max=70),
            temperature=round(random.uniform(36.1, 38.2), 1),
            blood_glucose=round(random.uniform(40.0, 140.0), 1),
            serum_bilirubin=round(random.uniform(4.0, 16.0), 1),
            murmurs=self.fake.boolean(chance_of_getting_true=10),
            abdominal_signs=self.fake.boolean(chance_of_getting_true=10),
            timestamp=int(time.time() * 1000),
        )
