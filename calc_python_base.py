# https://github.com/ifnesi/1brc#submitting
# Modified the multiprocessing version

def process_file(file_name: str):
    result = dict()

    with open(file_name, "rb") as f:
        for line in f:
            location, measurement = line.split(b";")
            measurement = float(measurement)
            if location not in result:
                result[location] = [
                    measurement,
                    measurement,
                    measurement,
                    1,
                ]
            else:
                _result = result[location]
                if measurement < _result[0]:
                    _result[0] = measurement
                if measurement > _result[1]:
                    _result[1] = measurement
                _result[2] += measurement
                _result[3] += 1

    print("{", end="")
    for location, measurements in sorted(result.items()):
        print(
            f"{location.decode('utf8')}={measurements[0]:.1f}/{(measurements[2] / measurements[3]) if measurements[3] !=0 else 0:.1f}/{measurements[1]:.1f}",
            end=", ",
        )
    print("\b\b} ")


if __name__ == "__main__":
    process_file("data/measurements.txt")