import duckdb
import time

print("Starting DuckDB baseline benchmark...")

# Connect to DuckDB
con = duckdb.connect("duckdb/taxi.duckdb")

queries = {
    "Total revenue per day": """
        SELECT
            DATE(pickup_datetime) AS day,
            SUM(total_amount) AS total_revenue
        FROM taxi_raw
        GROUP BY day
        ORDER BY day;
    """,

    "Average fare per passenger count": """
        SELECT
            passenger_count,
            AVG(fare_amount) AS avg_fare
        FROM taxi_raw
        GROUP BY passenger_count
        ORDER BY passenger_count;
    """,

    "Top 10 longest trips": """
        SELECT
            pickup_datetime,
            dropoff_datetime,
            trip_distance
        FROM taxi_raw
        ORDER BY trip_distance DESC
        LIMIT 10;
    """
}

results = {}

for name, query in queries.items():
    print(f"\nRunning query: {name}")

    start = time.time()
    con.execute(query).fetchall()
    end = time.time()

    elapsed = round(end - start, 4)
    results[name] = elapsed

    print(f"⏱️ Time taken: {elapsed} seconds")

print("\n=== DuckDB Baseline Benchmark Summary ===")
for name, timing in results.items():
    print(f"{name}: {timing} seconds")

con.close()
