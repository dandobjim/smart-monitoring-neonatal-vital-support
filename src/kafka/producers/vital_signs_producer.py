from dataclasses import asdict

import avro.schema
from confluent_kafka.avro import AvroProducer

from src.utils.vital_signs_simulator import VitalSignsSimulator

simulator = VitalSignsSimulator()
value_schema = avro.schema.parse(open("../schemas/vital_signs.avsc", "r").read())

conf = {
    "bootstrap.servers": "localhost:9092",
    "schema.registry.url": "http://localhost:8081",
}

producer = AvroProducer(conf, default_value_schema=value_schema)


def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Error trying to send the message: {err}")
    else:
        print(
            f"✅ Message sent to {msg.topic()} [{msg.partition()}] offset {msg.offset()}"
        )


while True:
    payload = simulator.simulate_vital_signs()

    producer.produce(
        topic="neonatal-vital-signs",
        value=asdict(payload),
        value_schema=value_schema,
        callback=delivery_report,
    )

    producer.flush()
