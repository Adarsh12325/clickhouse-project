DROP TABLE IF EXISTS taxi_raw;

CREATE TABLE taxi_raw (
    vendor_id TINYINT,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count TINYINT,
    trip_distance FLOAT,
    fare_amount FLOAT,
    total_amount FLOAT
);
