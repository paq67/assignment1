# app/db.py
# SQLite setup with SQLAlchemy
import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///orders.db")
engine = create_engine(DATABASE_URL, echo=False)
metadata = MetaData()

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order_id", Integer, nullable=False),
    Column("item", String, nullable=False),
)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Initialize the database and create tables."""
    metadata.create_all(engine)
