import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

result = client.query("SELECT 1")
print("✅ ClickHouse connection OK:", result.result_rows)
