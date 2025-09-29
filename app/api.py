# app/api.py
# Flask API exposing /order endpoint
import os
from flask import Flask, request, jsonify
from app.producer import publish_order
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json()
    if not data or "order_id" not in data or "item" not in data:
        return jsonify({"error": "Invalid payload. Must include order_id and item."}), 400
    if not isinstance(data["order_id"], int) or not isinstance(data["item"], str):
        return jsonify({"error": "order_id must be int and item must be str."}), 400
    publish_order({"order_id": data["order_id"], "item": data["item"]})
    return jsonify({"status": "Order published."}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
