from pymongo import MongoClient
from bson import ObjectId
from pprint import pprint
import time
import random


class Config(object):
    DATABASE_URI = "mongodb://localhost:27017/test"
    DATABASE = "test_db"


print(f"Connecting to: [{Config.DATABASE}]...")
client = MongoClient(Config.DATABASE_URI)
db = client[Config.DATABASE]
print(f"Connected: [{Config.DATABASE}]...")

client.drop_database(Config.DATABASE)


def generate_d():
    e = db.e.insert({"val": random.randint(0, 10)})
    return {"val": random.randint(0, 10), "e": e}


def generate_c():
    c = [
        {"d": [generate_d() for i in range(0, 2)], "val": 3}
        for i in range(0, 5)
    ]
    db.c.insert_many(c)
    return [o["_id"] for o in c]


def generate_b():
    b = [{"c": generate_c(), "val": 2} for i in range(0, 2)]
    db.b.insert_many(b)
    return [o["_id"] for o in b]


def generate_a():
    a = [{"b": generate_b(), "val": 1} for i in range(0, 2)]
    db.a.insert_many(a)
    return [o["_id"] for o in a]


# INSERT A BUNCH OF DOCUMENTS
start_time = time.time()
vals = [generate_a() for i in range(0, 200)]
print("Inserting took", str(time.time() - start_time) + "s")

# AGGREGATION PIPELINE
start_time = time.time()
res = db.a.aggregate(
    [
        {
            "$lookup": {
                "from": "b",
                "let": {"b": "$b"},
                "pipeline": [
                    {"$match": {"$expr": {"$in": ["$_id", "$$b"]}}},
                    {
                        "$lookup": {
                            "from": "c",
                            "let": {"c": "$c"},
                            "pipeline": [
                                {"$match": {"$expr": {"$in": ["$_id", "$$c"]}}},
                                {
                                    "$lookup": {
                                        "from": "e",
                                        "let": {"e": "$d.e"},
                                        "pipeline": [
                                            {
                                                "$match": {
                                                    "$expr": {
                                                        "$in": ["$_id", "$$e"]
                                                    }
                                                }
                                            }
                                        ],
                                        "as": "test",
                                    }
                                },
                                {
                                    "$addFields": {
                                        "d": {
                                            "$map": {
                                                "input": "$d",
                                                "in": {
                                                    "$mergeObjects": [
                                                        "$$this",
                                                        {
                                                            "e": {
                                                                "$arrayElemAt": [
                                                                    "$test",
                                                                    {
                                                                        "$indexOfArray": [
                                                                            "$test._id",
                                                                            "$$this.e",
                                                                        ]
                                                                    },
                                                                ]
                                                            }
                                                        },
                                                    ]
                                                },
                                            }
                                        }
                                    }
                                },
                                {"$project": {"test": False}},
                            ],
                            "as": "c",
                        }
                    },
                ],
                "as": "b",
            }
        }
    ]
)

i = 0
example = None
for r in res:
    if i == 0:
        example = r
    print(f"Found {i}")
    i += 1

pprint(example)


print(f"Found n records in", str(time.time() - start_time) + "s")

