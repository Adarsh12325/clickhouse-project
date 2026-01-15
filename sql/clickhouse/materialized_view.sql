CREATE MATERIALIZED VIEW IF NOT EXISTS mv_daily_revenue
ENGINE = SummingMergeTree
PARTITION BY toYYYYMM(day)        -- use 'day', which exists in SELECT
ORDER BY day
POPULATE AS
SELECT
    toDate(pickup_datetime) AS day,
    sum(total_amount) AS daily_revenue
FROM taxi_optimized
GROUP BY day;
