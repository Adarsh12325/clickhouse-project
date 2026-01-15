import clickhouse_connect
import pandas as pd
import glob

# Connect to ClickHouse (use the same password that worked before)
client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

# Read the optimized table SQL (optional: drop table before loading if needed)
files = glob.glob("data/parquet/*.parquet")

for file in files:
    print(f"Loading {file} into optimized table...")
    df = pd.read_parquet(file)

    # Select and rename columns
    df = df[
        [
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "passenger_count",
            "trip_distance",
            "total_amount"
        ]
    ]

    df.columns = [
        "pickup_datetime",
        "dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "total_amount"
    ]

    # Insert into optimized table
    client.insert_df("taxi_optimized", df)

print("✅ Data loaded into optimized table successfully")
