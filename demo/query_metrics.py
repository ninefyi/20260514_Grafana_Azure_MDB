import os
from datetime import datetime, timedelta, timezone

from pymongo import MongoClient

MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.getenv("MONGODB_DB", "observability")
COLLECTION = os.getenv("MONGODB_COLLECTION", "app_events")

client = MongoClient(MONGODB_URI)
coll = client[DB_NAME][COLLECTION]

window_start = datetime.now(timezone.utc) - timedelta(minutes=5)

pipeline = [
    {"$match": {"ts": {"$gte": window_start}, "environment": "prod-sg"}},
    {
        "$group": {
            "_id": {"service": "$service", "level": "$level"},
            "count": {"$sum": 1},
            "p95_latency": {"$percentile": {"input": "$latency_ms", "p": [0.95]}},
        }
    },
    {"$sort": {"count": -1}},
]

for row in coll.aggregate(pipeline, allowDiskUse=True):
    print(row)
