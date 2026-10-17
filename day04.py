from components import Capacitor, Circuit, Inductor, Resistor

r1 = Resistor("R1", 100)
print(r1)
print(r1.current(5))
print(r1.is_overloaded(5))
print(Resistor("R2", 47).is_overloaded(5))
print("\n*********************************\n")

parts = [Resistor("R1", 470), Resistor("R2", 100), Resistor("R3", 220)]
print(sorted(parts))
print(Resistor("A", 100) == Resistor("B", 100))

print("\n*********************************\n")

r = Resistor("R1", 10_000)
c = Capacitor("C1", 100e-9)
print(r.impedance(159.15))
print(c.impedance(159.15))
print(abs(c.impedance(159.15)))

print("\n*********************************\n")

r = Resistor("R1", 100)
# try:
#    r.ohms = 0
# except ValueError as e:
#    print("Caught:", e)
print("\n*********************************\n")

coil = Inductor("L1", 0.010)
print(coil.impedance(1_000))

print("\n*********************************\n")

circuit = Circuit([Resistor("R1", 10_000), Capacitor("C1", 100e-9)])
z = circuit.series_impedance(159.15)
print(z)
print(abs(z))
print("\n*********************************\n")

print(f"{circuit.rc_lowpass_gain(159.15):.4f}")

print("\n*********************************\n")

freqs = [10, 100, 1_000, 10_000, 100_000]
for f in freqs:
    gain = circuit.rc_lowpass_gain(f)
    print(f"{f:>7} Hz gain = {gain:.4f}")
