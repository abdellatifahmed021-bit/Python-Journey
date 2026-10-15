import csv
import random
from datetime import datetime
from pathlib import Path

HEADER = ["timestamp", "voltage"]


def log_reading(path, voltage):
    path = Path(path)
    write_header = not path.exists()
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(HEADER)
        stamp = datetime.now().isoformat(timespec="seconds")
        writer.writerow([stamp, f"{voltage:.3f}"])


def load_readings(path):
    readings = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        next(reader, None)
        for line_no, row in enumerate(reader, start=2):
            try:
                timestamp, voltage = row
                readings.append((timestamp, float(voltage)))
            except ValueError:
                print(f"Warning: skipping malformed row {line_no} : {row}")
    return readings


def summarize(readings):
    if not readings:
        raise ValueError("No readings to summarize")
    volts = [v for _, v in readings]
    return min(volts), max(volts), sum(volts) / len(volts)


if __name__ == "__main__":
    path = Path("readings.csv")
    for _ in range(5):
        log_reading(path, random.uniform(3.2, 3.4))
    print("Logged 5 readings")

    readings = load_readings(path)
    lo, hi, mean = summarize(readings)
    print(f"Min: {lo:.2f} V | Max: {hi:.2f} V | Mean: {mean:.2f} V")
