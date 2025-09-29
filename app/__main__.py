# app/__main__.py
# Entrypoint for running consumer
from app.consumer import consume_orders

if __name__ == "__main__":
    consume_orders()
