import math
import random
from pathlib import Path
from datetime import datetime


def series_resistance(values):
    return sum(values)


def parallel_resistance(values):
    if not values:
        raise ValueError("Need at least one resistor")
    if any(r == 0 for r in values):
        raise ValueError("Resistance cannot be zero")
    return 1 / sum(1 / r for r in values)


def voltage_divider(vin, r1, r2):
    return vin * r2 / (r1 + r2)


def rc_time_constant(r: float, c: float) -> float:
    return r * c


def rc_cutoff(r: float, c: float) -> float:
    return 1 / (2 * math.pi * r * c)


if __name__ == "__main__":
    print(series_resistance([100, 100]))
    print(parallel_resistance([100, 100]))
    # print(parallel_resistance([]))
    # print(parallel_resistance([0, 100]))
    print(math.sqrt(2), random.choice([1, 2, 3]), datetime.now())
