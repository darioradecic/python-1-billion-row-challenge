# Code credits: https://github.com/ifnesi/1brc#submitting

import polars as pl

df = (
    pl.scan_csv("data/measurements.txt", separator=";", has_header=False, with_column_names=lambda cols: ["station_name", "measurement"])
        .group_by("station_name")
        .agg(
            pl.min("measurement").alias("min_measurement"),
            pl.mean("measurement").alias("mean_measurement"),
            pl.max("measurement").alias("max_measurement")
        )
        .sort("station_name")
        .collect(streaming=True)
)

print("{", end="")
for row in df.iter_rows():
    print(
        f"{row[0]}={row[1]:.1f}/{row[2]:.1f}/{row[3]:.1f}", 
        end=", "
    )
print("\b\b} ")