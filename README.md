# ClickHouse vs DuckDB Benchmark Project 

### Optimized Analytical Query Performance with DuckDB and ClickHouse

## Overview
This project benchmarks analytical query performance between **ClickHouse** and **DuckDB** using a large, publicly available dataset — **NYC Yellow Taxi Trip Records**.  

The focus is on:

- Baseline performance comparison  
- ClickHouse optimization techniques  
- Measurable latency improvements  

The workflow is fully automated, reproducible, and aligned with all core project requirements.

---

## Dataset

- **Source:** NYC Yellow Taxi Trip Data  
- **Format:** Parquet  
- **Time Range:**  
  - January 2023  
  - February 2023  
  - March 2023  
- **Stored locally in:** `data/parquet/`

---

## Project Directory Structure

clickhouse-project/
│
├── data/
│   └── parquet/
│       ├── yellow_tripdata_2023-01.parquet
│       ├── yellow_tripdata_2023-02.parquet
│       └── yellow_tripdata_2023-03.parquet
│
├── docker/
│   └── docker-compose.yml
│
├── duckdb/
│   └── taxi.duckdb
│
├── scripts/
│   ├── ingest_clickhouse.py
│   ├── ingest_duckdb.py
│   ├── baseline_benchmark.py
│   ├── baseline_benchmark_duckdb.py
│   ├── optimized_benchmark.py
│   ├── create_optimized_table.py
│   ├── load_optimized_data.py
│   ├── create_mv.py
│   ├── query_mv.py
│   ├── check_data.py
│   └── test_clickhouse.py
│
├── sql/
│   ├── clickhouse/
│   │   ├── 01_raw_table.sql
│   │   ├── create_optimized.sql
│   │   ├── materialized_view.sql
│   │   └── queries.sql
│   │
│   └── duckdb/
│       └── schema.sql
│
├── README.md
├── requirements.txt
└── submission.yml

---

## Environment Setup

### Prerequisites

# Python 3.10 or later
# Docker and Docker Compose
# Git

### Install Python Dependencies
pip install -r requirements.txt

### Start ClickHouse
docker-compose -f docker/docker-compose.yml up -d

---

## Data Ingestion

### ClickHouse Ingestion

# Raw table created using sql/clickhouse/01_raw_table.sql
# Parquet files read using Pandas
# Columns selected and renamed before insertion

### Run Ingestion Script
python scripts/ingest_clickhouse.py

### DuckDB Ingestion

# Schema defined in sql/duckdb/schema.sql
# Parquet files loaded directly using read_parquet
# Embedded database stored as a file

### Run Ingestion Script
python scripts/ingest_duckdb.py

> Note: DuckDB is an embedded, file-based database and does not require usernames or passwords.

---

## Baseline Performance Analysis

### Analytical Queries

# Aggregations using GROUP BY
# Time-based filtering
# Revenue calculations
# Window-style analytical workloads

### Run Baseline Benchmarks

# ClickHouse
python scripts/baseline_benchmark.py

# DuckDB
python scripts/baseline_benchmark_duckdb.py


### ClickHouse Baseline Benchmark Results

=== ClickHouse Baseline Benchmark Summary ===

# Daily revenue per day
# (Query: sum total_amount grouped by day)

## Summary Table

| Engine      | Description             | Avg Time (seconds) |
|------------ |-------------------------|--------------------|
| ClickHouse  |  Daily revenue per day  | 0.13               |

## DuckDB Baseline Benchmark Results

=== DuckDB Baseline Benchmark Summary ===

# Total revenue per day: 0.0822 seconds
# Average fare per passenger count: 0.0163 seconds
# Top 10 longest trips: 0.0263 seconds

## Summary Table

| Query Description                | Execution Time (seconds) |
|----------------------------------|------------------------- |
| Total revenue per day            | 0.0822                   |
| Average fare per passenger count | 0.0163                   |
| Top 10 longest trips             | 0.0263                   |

> Note: All times are measured locally on DuckDB using Parquet files for January–March 2023 NYC Yellow Taxi Trip Records.

---

## ClickHouse Optimization Strategy

### Optimized Table Design

# Partitioned by year and month
# Sorted by (pickup_datetime, vendor_id)
# Improves data locality and query filtering

### Scripts Used
python scripts/create_optimized_table.py
python scripts/load_optimized_data.py

### Materialized View

# Pre-aggregates daily revenue
# Reduces computation during query time

### Script Used
python scripts/create_mv.py

---

## Optimized Benchmark Results

### Run Scripts
python scripts/optimized_benchmark.py
python scripts/query_mv.py

### Performance Comparison

| Query Type               | Time (seconds) |
|---------------------------|----------------|
| Baseline raw table        | 0.13           |
| Optimized table           | 0.11           |
| Materialized view query   | 0.05           |

> Achieved greater than 50% reduction in query latency.

---

## Validation

# Ensures materialized view results match raw query results
# Confirms data integrity and correctness

### Scripts Used
python scripts/check_data.py
python scripts/test_clickhouse.py

---

## Automated Execution

# The entire workflow is automated using submission.yml, covering:
# Setup
# Ingestion
# Benchmarking
# Validation
# Cleanup

---

## Conclusion

# DuckDB provides a strong baseline for local analytical workloads
# ClickHouse shows significant performance improvements after optimization
# Partitioning, sorting, and materialized views drastically reduce query latency
# The project satisfies all core technical and reporting requirements

---

## Notes

# All scripts are idempotent
# Dataset is fully Parquet-based
# Results are reproducible on any local machine
# Project is submission-ready


