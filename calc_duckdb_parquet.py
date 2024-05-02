import duckdb

with duckdb.connect() as conn:
    data = conn.sql("""
        select
            station_name,
            min(measurement) as min_measurement,
            cast(avg(measurement) as decimal(8, 1)) as mean_measurement,
            max(measurement) as max_measurement
        from parquet_scan('data/measurements.parquet')
        group by station_name
        order by station_name
    """)

    print("{", end="")
    for row in sorted(data.fetchall()):
        print(
            f"{row[0]}={row[1]}/{row[2]}/{row[3]}",
            end=", ",
        )
    print("\b\b} ")