import sqlite3

import time


conn = sqlite3.connect("./cache/identity_cache.sqlite")
c = conn.cursor()


def clear_cache():
    pass


def create_table_if_not_exists(name):

    res = c.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';"
    )

    if not c.fetchone():
        c.execute(f"CREATE TABLE '{name}' (name text, real text);")
    else:
        print("Table already exists")


create_table_if_not_exists("test")

n = 1000000

start_time = time.time()
for i in range(0, n):
    c.execute(
        f"INSERT INTO test (name, real) VALUES ('TestName', '{','.join(['0.008570062445832943' for i in range(0, 511)])}');"
    )
conn.commit()
print(f"Inserted {n} records in {time.time() - start_time}")

start_time = time.time()
res2 = c.execute(f"SELECT COUNT(*) AS count FROM test;")
count = 0
for r in res2:
    count = r[0]
print(f"Counted {count} records in {time.time() - start_time}")

start_time = time.time()
res2 = c.execute(f"SELECT name, real FROM test;")
res2 = list(res2)

print(f"Read {count} records in {time.time() - start_time}")
