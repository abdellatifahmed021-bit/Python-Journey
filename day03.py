# from math import pi

from pathlib import Path
import csv
import json
import circuits


def voltage_divider(vin, r1, r2=1000):
    return vin * r2 / (r1 + r2)


print(voltage_divider(5, 1000))
print(voltage_divider(5, 1000, 2200))
print(voltage_divider(vin=5, r2=2200, r1=1000))

print("\n****************************************\n")


def average(*values):
    return sum(values) / len(values)


print(average(3.3, 3.1, 3.4))

print("\n****************************************\n")


def describe(component, **specs):
    print(component)
    for key, val in specs.items():
        print(f" {key}: {val}")


describe("Capacitor", farads=100e-6, voltage_rating=25, type="electrolytic")

print("\n****************************************\n")


def min_max(values):
    return min(values), max(values)


lo, hi = min_max([4.9, 5.1, 5.0])
print(lo, hi)
print("\n****************************************\n")


# def rc_time_constant(r: float, c: float) -> float:
#    return r * c


# print(rc_time_constant(10_000, 100e-6))

# print("\n****************************************\n")


# def rc_cutoff(r: float, c: float) -> float:
#    return 1 / (2 * pi * r * c)


# print(f"{rc_cutoff(10_000, 100e-9):.2f} Hz")

print("\n****************************************\n")


def total_power(*powers_w: float, efficiency: float = 1.0) -> float:
    if efficiency <= 0:
        raise ValueError("Efficiency must be positive")
    return sum(powers_w) / efficiency


print(total_power(10, 20, 30))
print(total_power(10, 20, 30, efficiency=0.9))
print(total_power(*[5, 5, 5], efficiency=0.5))

print("\n****************************************\n")


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None


print(safe_divide(10, 0))
print(safe_divide(10, 2))
print("\n****************************************\n")


def parse_voltage(text):
    try:
        v = float(text)
    except ValueError:
        print(f"'{text}' is not a number")
    else:
        return v
    finally:
        print("parse attempt finished")


print(parse_voltage("3.3"))
print(parse_voltage("3.3V"))

print("\n****************************************\n")


def validate_resistance(r):
    if r <= 0:
        raise ValueError(f"Resistance must be postive, got{r}")
    return r


try:
    validate_resistance(-5)
except ValueError as e:
    print("Caught:", e)
print("\n****************************************\n")


def read_float(prompt: str) -> float:
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print(f"'{text}'is not a number, try again.")


# voltage = read_float("supply voltage (V): ")
# print(f"You entered {voltage} V")

print(circuits.series_resistance([100, 200]))
print(circuits.parallel_resistance([220, 330]))
print(circuits.random.choice([1, 2, 3]))
print(circuits.rc_time_constant(10_000, 100e-6))
print(circuits.rc_cutoff(10_000, 100e-9))

data_file = Path("measurement.txt")
with open(data_file, "w") as f:
    f.write("3.30\n3.28\n3.31\n3.29\n")

with open(data_file) as f:
    readings = [float(line) for line in f]
print(readings)

with open(data_file, "a") as f:
    f.write("3.30\n")

print(data_file.exists())
text = data_file.read_text()
print(len(text.splitlines()), "lines")


rows = [
    {"name": "R1", "ohms": 100, "watts": 0.25},
    {"name": "R2", "ohms": 220, "watts": 0.5},
    {"name": "R3", "ohms": 470, "watts": 0.25},
]

with open("parts.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "ohms", "watts"])
    writer.writeheader()
    writer.writerows(rows)

with open("parts.csv", newline="") as f:
    reader = csv.DictReader(f)
    parts = [
        {"name": r["name"], "ohms": int(r["ohms"]), "watts": float(r["watts"])}
        for r in reader
    ]
print(parts)

with open("parts.json", "w") as f:
    json.dump(parts, f, indent=2)
with open("parts.json") as f:
    loaded = json.load(f)
print(loaded == parts)


def load_parts(path):
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            return [
                {"name": r["name"], "ohms": int(r["ohms"]), "watts": float(r["watts"])}
                for r in reader
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Parts file not found: {path}") from None


print(load_parts("parts.csv"))

try:
    load_parts("wrong_name.csv")
except FileNotFoundError as e:
    print("Caught", e)
