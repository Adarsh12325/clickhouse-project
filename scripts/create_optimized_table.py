import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password='clickhouse123'
)


with open('sql/clickhouse/create_optimized.sql', 'r') as f:
    query = f.read()

client.command(query)

print("Optimized table created successfully")
