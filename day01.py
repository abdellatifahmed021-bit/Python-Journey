def ohms_law_current(voltage, resistance):
    """Return current in amps given voltage (V) and resistance (Ω)."""
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance


def power_dissipated(voltage, current):
    """Return power in watts given voltage (V) and current (A)."""
    return voltage * current


def series_resistance(resistors):
    return sum(resistors)


def parallel_resistance(resistors):
    if not resistors or any(r == 0 for r in resistors):
        raise ValueError("Resistor list cannot be empty.")
    return 1 / sum(1 / r for r in resistors)


resistors = [100, 220, 470, 1000]  # ohms
supply = 5.0  # volts

for r in resistors:
    i = ohms_law_current(supply, r)
    p = power_dissipated(supply, i)
    print(f"R = {r:>5} ohm | I = {i * 1000:7.2f} mA | P = {p * 1000:7.2f} mW")

print()
resistor_values = {"R1": 100, "R2": 220, "R3": 470, "R4": 1000}

for r, value in resistor_values.items():
    i = ohms_law_current(supply, value)
    print(f"{r}: {value:>5} ohm -> {i * 1000:7.2f} mA")

print()
values = list(resistor_values.values())
print(f"Series: {series_resistance(values):.2f} ohms")
print(f"Parallel: {parallel_resistance(values):.2f} ohms")

assert series_resistance([100, 200, 300]) == 600
assert parallel_resistance([100, 100]) == 50
print("\nAll tests passed!")
