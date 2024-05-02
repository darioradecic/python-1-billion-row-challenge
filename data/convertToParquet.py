import pandas as pd

df = pd.read_csv("measurements.txt", sep=";", header=None, names=["station_name", "measurement"], engine="pyarrow")
df.to_parquet("measurements.parquet")