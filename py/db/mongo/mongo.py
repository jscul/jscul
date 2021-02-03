from pymongo import MongoClient
from bson import ObjectId
from pprint import pprint


class Config(object):
    DATABASE_URI = "mongodb://localhost:27017/test"
    DATABASE = "test_db"


print(f"Connecting to: [{Config.DATABASE}]...")
client = MongoClient(Config.DATABASE_URI)
db = client[Config.DATABASE]
print(f"Connected: [{Config.DATABASE}]...")


def generate_doc():
    return {"a": 1, "b": 2, "c": 3}


# INSERT A BUNCH OF DOCUMENTS
db.test_collection.insert_many([generate_doc() for i in range(0, 5)])

# AGGREGATION PIPELINE
pprint(list(db.test_collection.aggregate([])))


client.drop_database(Config.DATABASE)
