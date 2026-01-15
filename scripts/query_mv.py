import time
import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

query = "SELECT * FROM mv_daily_revenue ORDER BY day"

print("Running query on materialized view...")

start = time.time()
client.query(query)
end = time.time()

print(f"⏱️ Query time on MV: {end - start:.2f} seconds")
