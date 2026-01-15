import clickhouse_connect
import pandas as pd
import glob

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

client.command("DROP TABLE IF EXISTS taxi_raw")

with open("sql/clickhouse/01_raw_table.sql") as f:
    client.command(f.read())

files = glob.glob("data/parquet/*.parquet")

for file in files:
    print(f"Loading {file}...")
    df = pd.read_parquet(file)

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

    df.columns = [
        "vendor_id",
        "pickup_datetime",
        "dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "fare_amount",
        "total_amount",
    ]

    client.insert_df("taxi_raw", df)

print("✅ ClickHouse RAW data loaded successfully")
