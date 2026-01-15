import time
import clickhouse_connect

# Connect to ClickHouse
client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

# Optimized query
query = """
SELECT
    toDate(pickup_datetime) AS day,
    sum(total_amount) AS daily_revenue
FROM taxi_optimized
GROUP BY day
ORDER BY day
"""

print("Running optimized query...")

start_time = time.time()
client.query(query)
end_time = time.time()

elapsed = end_time - start_time

print(f"⏱️ Optimized query time: {elapsed:.2f} seconds")
