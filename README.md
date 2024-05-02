# Python 1 Billion Row Challenge

- A couple of different solutions for the original [challenge](https://1brc.dev)
- Most of the code was taken from the [official Python submission repo](https://github.com/ifnesi/1brc#submitting)
- Some parts were modified, some were written from scratch

## How to Get Started
1. Clone the repo
2. Install the packages - `pip install -r requirements.txt` (preferrably in a new virtual environment)
3. Create your `measurements.txt` file - `cd data` - `python createMeasurements.py`
4. [OPTIONAL] - convert to Parquet - `cd data` - `python convertToParquet.py`
5. Run the script(s)

For the PyPy script, you'll need to [install PyPy](https://doc.pypy.org/en/latest/install.html) first.

## My Results
- I've ran all the scripts 3 times on my M3 Pro Macbook Pro 16" with 12 CPU cores and 36 GB of RAM
- You'll find the runtime results below

### Pure Python
- 230.83s user 3.18s system 99% cpu 3:54.46 total
- 230.54s user 2.83s system 99% cpu 3:53.77 total
- 232.71s user 2.92s system 99% cpu 3:55.92 total

### Python Multiprocessing
- 391.53s user 5.19s system 1165% cpu 34.026 total
- 393.52s user 5.31s system 1103% cpu 36.143 total
- 392.46s user 5.23s system 1169% cpu 33.995 total

### PyPy
- 197.62s user 5.57s system 1128% cpu 17.999 total
- 197.08s user 5.51s system 1148% cpu 17.638 total
- 196.85s user 5.50s system 1136% cpu 17.807 total

### Pandas
- 113.84s user 38.96s system 74% cpu 3:24.78 total
- 113.91s user 37.91s system 78% cpu 3:13.03 total
- 114.06s user 36.83s system 80% cpu 3:07.82 total

### Dask
- 117.61s user 10.32s system 350% cpu 36.549 total
- 117.29s user 9.10s system 370% cpu 34.131 total
- 117.01s user 9.22s system 367% cpu 34.323 total

### Polars
- 78.25s user 3.89s system 912% cpu 9.001 total
- 78.10s user 3.94s system 910% cpu 9.014 total
- 78.20s user 3.85s system 913% cpu 8.981 total

### DuckDB
- 95.71s user 1.53s system 1086% cpu 8.949 total
- 95.66s user 1.55s system 1141% cpu 8.514 total
- 95.24s user 1.54s system 1132% cpu 8.544 total

### Pandas (Parquet)
- 62.57s user 18.35s system 79% cpu 1:41.71 total
- 61.81s user 18.16s system 80% cpu 1:39.11 total
- 62.09s user 22.21s system 78% cpu 1:47.55 total

### Dask (Parquet)
- 47.09s user 32.01s system 416% cpu 18.983 total
- 47.57s user 31.23s system 427% cpu 18.424 total
- 47.22s user 31.11s system 425% cpu 18.419 total

### Polars (Parquet)
- 46.25s user 5.21s system 792% cpu 6.496 total
- 46.66s user 4.87s system 866% cpu 5.949 total
- 46.89s user 4.81s system 872% cpu 5.926 total

### DuckDB (Parquet)
- 43.18s user 0.62s system 1138% cpu 3.847 total
- 42.90s user 0.61s system 1113% cpu 3.907 total
- 42.96s user 0.61s system 1128% cpu 3.862 total