# Flask Kafka Orders API

Production-ready Python/Flask API with Kafka, SQLite, and Codespaces support.

## Features
- **Flask API**: POST `/order` endpoint publishes orders to Kafka
- **Kafka Consumer**: Listens to `orders` topic, inserts into SQLite
- **SQLite**: Persists orders
- **Docker Compose**: Runs Flask, Kafka, Zookeeper
- **Devcontainer**: Ready for GitHub Codespaces

## Setup

### 1. Clone & Configure
```bash
git clone <repo-url>
cd <repo>
cp .env.example .env
```

### 2. Run with Docker Compose
```bash
docker-compose up --build
```
- Flask API: [http://localhost:8000/order](http://localhost:8000/order)
- Kafka: localhost:9092
- Zookeeper: localhost:2181

### 3. Codespaces/Devcontainer
- Open in GitHub Codespaces or VS Code with Dev Containers
- Requirements auto-installed, DB initialized

### 4. API Usage
```bash
curl -X POST http://localhost:8000/order \
  -H "Content-Type: application/json" \
  -d '{"order_id": 123, "item": "Widget"}'
```

### 5. Run Consumer
In a separate terminal (inside devcontainer):
```bash
python -m app.consumer
```

### 6. Run Tests
```bash
pytest tests/
```

## Environment Variables
See `.env.example` for required variables.

## Notes
- Kafka/Zookeeper use Bitnami images
- Orders table auto-created on startup
- For production, review security and scaling
