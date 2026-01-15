SELECT
    toDate(pickup_datetime) AS day,
    sum(total_amount) AS daily_revenue
FROM taxi_raw
GROUP BY day
ORDER BY day
