import time
import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

with open("sql/clickhouse/queries.sql") as f:
    query = f.read()

print("Running baseline query...")

start_time = time.time()
client.query(query)
end_time = time.time()

elapsed = end_time - start_time

print(f"⏱️ Baseline query time: {elapsed:.2f} seconds")
