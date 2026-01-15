import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

result = client.query("SELECT count(*) FROM taxi_raw")
print("Total rows in taxi_raw:", result.result_rows)
