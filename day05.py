from components import Resistor, Capacitor, Circuit
import matplotlib.pyplot as plt
import numpy as np

resistors = np.array([100, 220, 470, 1000])
currents = 5 / resistors
power = 5 * currents
print(currents * 100)
print(power)

print("\n*********************************\n")

print(np.linspace(0, 1, 5))
print(np.logspace(1, 5, 5))
print(np.arange(0, 10, 2))

print("\n*********************************\n")

v = np.array([3.29, 3.31, 3.30, 3.28, 3.33])
print(v.mean(), v.std(), v.min(), v.max(), v.argmax())

print("\n*********************************\n")

print(resistors[resistors > 200])
print(resistors[power > 0.05])

print("\n*********************************\n")

grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid.shape)
print(grid.sum(axis=0))
print(grid.sum(axis=1))

print("\n*********************************\n")

z = np.array([3 + 4j, 1 - 1j])
print(np.abs(z))
print(np.degrees(np.angle(z)))


t = np.linspace(0, 0.1, 1000, endpoint=False)
v_mains = 230 * np.sqrt(2) * np.sin(2 * np.pi * 50 * t)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t * 1000, v_mains, label="Mains Voltage")
ax.set_xlabel("Time(ms)")
ax.set_ylabel("Voltage(V)")
ax.set_title("50 Hz AC Waveform")
ax.grid(True)
ax.legend()
fig.savefig("mains.png", dpi=150)
plt.show()


R = 10_000
C = 100e-9
f = np.logspace(1, 5, 500)
H = 1 / (1 + 2j * np.pi * f * R * C)
gain_db = 20 * np.log10(np.abs(H))
phase_deg = np.degrees(np.angle(H))
fc = 1 / (2 * np.pi * R * C)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

ax1.semilogx(f, gain_db)
ax1.axhline(-3, color="gray", linestyle="--", label="-3 dB")
ax1.axvline(fc, color="red", linestyle=":", label=f"fc = {fc:.0f} Hz")
ax1.set_ylabel("Gain (dB)")
ax1.set_title("RC Low-Pass Filter: Bode Plot")
ax1.grid(True, which="both", alpha=0.4)
ax1.legend()

ax2.semilogx(f, phase_deg)
ax2.axvline(fc, color="red", linestyle=":")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Phase (degrees)")
ax2.grid(True, which="both", alpha=0.4)

fig.tight_layout()
fig.savefig("bode_rc_lowpass.png", dpi=150)
plt.show()

print("\n*********************************\n")

names = np.array(["R1", "R2", "R3", "R4"])
resistors = np.array([100, 220, 470, 1000])
supply = 12  # volts

power = supply**2 / resistors
print(power)
print(names[power > 0.25])

print("\n*********************************\n")

rng = np.random.default_rng(0)  # seeded, so results repeat
v_noisy = v_mains + rng.normal(0, 20, t.size)


def rms(x):
    return np.sqrt(np.mean(x**2))


print(f"Clean RMS: {rms(v_mains):.2f} V")  # 230.00
print(f"Noisy RMS: {rms(v_noisy):.2f} V")  # about 231

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t * 1000, v_noisy, color="lightgray", label="Noisy")
ax.plot(t * 1000, v_mains, color="tab:blue", label="Clean")
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Voltage (V)")
ax.legend()
ax.grid(True)
plt.show()

print("\n*********************************\n")

idx = np.argmin(np.abs(gain_db + 3))
print(f"Closest to -3 dB: {f[idx]:.1f} Hz (gain {gain_db[idx]:.2f} dB)")
print(f"Calculated fc:    {fc:.1f} Hz")

print("\n*********************************\n")

fig, ax = plt.subplots(figsize=(8, 4))

for cap in (10e-9, 100e-9, 1e-6):
    H_cap = 1 / (1 + 2j * np.pi * f * R * cap)
    fc_cap = 1 / (2 * np.pi * R * cap)
    ax.semilogx(
        f,
        20 * np.log10(np.abs(H_cap)),
        label=f"C = {cap * 1e9:g} nF (fc = {fc_cap:.0f} Hz)",
    )

ax.axhline(-3, color="gray", linestyle="--")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Gain (dB)")
ax.set_title("Effect of Capacitance on Cutoff Frequency")
ax.grid(True, which="both", alpha=0.4)
ax.legend()
plt.show()

print("\n*********************************\n")


circuit = Circuit([Resistor("R1", R), Capacitor("C1", C)])
gain_from_classes = np.array([circuit.rc_lowpass_gain(x) for x in f])
gain_from_formula = np.abs(H)

print("Classes match formula:", np.allclose(gain_from_classes, gain_from_formula))
