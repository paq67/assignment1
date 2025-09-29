# app/consumer.py
# Kafka consumer for 'orders' topic, inserts into SQLite
import os
import json
from kafka import KafkaConsumer
from app.db import SessionLocal, orders
from sqlalchemy import insert
from dotenv import load_dotenv

load_dotenv()
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///orders.db")

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers=KAFKA_BOOTSTRAP,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="order-consumer-group",
)

def consume_orders():
    """Consume orders from Kafka and insert into DB."""
    session = SessionLocal()
    for msg in consumer:
        order = msg.value
        stmt = insert(orders).values(order_id=order["order_id"], item=order["item"])
        session.execute(stmt)
        session.commit()
        print(f"Inserted order: {order}")
