# tests/test_api.py
import os
import pytest
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000/order")

def test_create_order():
    payload = {"order_id": 1, "item": "Widget"}
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "Order published."
