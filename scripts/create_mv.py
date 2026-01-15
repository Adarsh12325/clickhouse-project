import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)

with open('sql/clickhouse/materialized_view.sql', 'r') as f:
    query = f.read()

client.command(query)

print("✅ Materialized view created and populated successfully")
