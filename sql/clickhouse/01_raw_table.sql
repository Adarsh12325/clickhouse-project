CREATE TABLE IF NOT EXISTS taxi_raw
(
    vendor_id UInt8,
    pickup_datetime DateTime,
    dropoff_datetime DateTime,
    passenger_count UInt8,
    trip_distance Float32,
    fare_amount Float32,
    total_amount Float32
)
ENGINE = MergeTree
ORDER BY tuple();
