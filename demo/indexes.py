import os

from pymongo import ASCENDING, DESCENDING, MongoClient

MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.getenv("MONGODB_DB", "observability")
COLLECTION = os.getenv("MONGODB_COLLECTION", "app_events")

client = MongoClient(MONGODB_URI)
coll = client[DB_NAME][COLLECTION]

coll.create_index([("ts", DESCENDING)])
coll.create_index([("service", ASCENDING), ("ts", DESCENDING)])
coll.create_index([("environment", ASCENDING), ("level", ASCENDING), ("ts", DESCENDING)])
coll.create_index([("route", ASCENDING), ("ts", DESCENDING)])

print("Indexes created")
