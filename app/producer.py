# app/producer.py
# Kafka producer for 'orders' topic
import os
from kafka import KafkaProducer
import json
from dotenv import load_dotenv

load_dotenv()
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def publish_order(order):
    """Publish order to Kafka 'orders' topic."""
    producer.send("orders", order)
    producer.flush()
