CREATE TABLE IF NOT EXISTS taxi_optimized
(
    pickup_datetime DateTime,
    dropoff_datetime DateTime,
    passenger_count UInt8,
    trip_distance Float32,
    total_amount Float32
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(pickup_datetime)
ORDER BY pickup_datetime
