import duckdb
import pandas as pd
import glob
import os

print("Starting DuckDB ingestion...")

# Ensure folder exists
os.makedirs("duckdb", exist_ok=True)

# Connect to DuckDB
con = duckdb.connect("duckdb/taxi.duckdb")

# Drop & create table (idempotent)
with open("sql/duckdb/schema.sql") as f:
    con.execute(f.read())

print("DuckDB schema created.")

files = glob.glob("data/parquet/*.parquet")

for file in files:
    print(f"Loading {file}...")

    df = pd.read_parquet(file)

    # Select SAME columns as ClickHouse
    df = df[
        [
            "VendorID",
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "passenger_count",
            "trip_distance",
            "fare_amount",
            "total_amount",
        ]
    ]

    # Rename columns to match schema
    df.columns = [
        "vendor_id",
        "pickup_datetime",
        "dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "fare_amount",
        "total_amount",
    ]

    con.register("temp_df", df)
    con.execute("INSERT INTO taxi_raw SELECT * FROM temp_df")
    con.unregister("temp_df")

# Row count check
row_count = con.execute("SELECT COUNT(*) FROM taxi_raw").fetchone()[0]
print(f"✅ DuckDB data loaded successfully. Row count: {row_count}")

con.close()
