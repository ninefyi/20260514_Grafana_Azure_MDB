import os
import random
from datetime import datetime, timezone

from faker import Faker
from pymongo import MongoClient

fake = Faker()

MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.getenv("MONGODB_DB", "observability")
COLLECTION = os.getenv("MONGODB_COLLECTION", "app_events")

client = MongoClient(MONGODB_URI, appname="grafana-observability-demo")
coll = client[DB_NAME][COLLECTION]

services = ["checkout-api", "catalog-api", "payments-worker"]
levels = ["INFO", "WARN", "ERROR"]
routes = ["/api/checkout", "/api/catalog", "/api/payments"]


def generate_event() -> dict:
    level = random.choices(levels, weights=[75, 18, 7], k=1)[0]
    latency = int(random.gauss(220, 90))
    latency = max(latency, 5)
    status = 200 if level == "INFO" else random.choice([400, 429, 500, 503])

    return {
        "ts": datetime.now(timezone.utc),
        "service": random.choice(services),
        "environment": "prod-sg",
        "level": level,
        "latency_ms": latency,
        "status_code": status,
        "route": random.choice(routes),
        "trace_id": fake.uuid4().replace("-", "")[:16],
        "message": fake.sentence(nb_words=5),
    }


def main(batch_size: int = 200) -> None:
    events = [generate_event() for _ in range(batch_size)]
    result = coll.insert_many(events)
    print(f"Inserted {len(result.inserted_ids)} events")


if __name__ == "__main__":
    main()
