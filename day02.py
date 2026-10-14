part = " Resistor R1: 220 ohm, 5% tolerance "
print(part.strip())
print(part.strip().upper())
print(part.strip().split(","))
print("220" in part)
print(part.strip().replace("ohm", "Ω"))

print("\n***********************************\n")

name = "R1"
value = 220
print(f"{name} = {value} ohm")
print(f"{value:08.3f}")
print(f"{4700:,}")
print(f"{0.00047:.2e}")

print("\n***********************************\n")

code = "R1-220-5%"
print(code[0:2])
print(code[-2:])
print(code[::-1])

print("\n***********************************\n")

line = "R3,470,0.25"
name, ohms, watts = line.split(",")
part = {"name": name, "ohms": int(ohms), "watts": float(watts)}
print(part)


print("\n***********************************\n")

values = [470, 100, 1000, 220]
print(values)
values.append(4700)
values.insert(0, 10)
values.remove(1000)
print(values)

print(sorted(values))
values.sort(reverse=True)
print(values)

print(len(values), min(values), max(values), sum(values))

print("\n***********************************\n")

print(values[:3])
print(values[-2:])

print("\n***********************************\n")

a = [1, 2, 3]
print(a)
b = a
b.append(4)
print(a)
print(b)
c = a.copy()
print(c)

print("\n***********************************\n")

series = [100, 150, 220, 330, 470, 680, 1000]


def closest_standard(value, series):

    return min(series, key=lambda s: abs(s - value))


print(closest_standard(400, series))

print("\n***********************************\n")

r = {"name": "R1", "ohms": 220, "watts": 0.25}
print(r["ohms"])
print(r.get("tolerance", 5))
r["tolerance"] = 1
print(r)
del r["watts"]
print(r)

for key, val in r.items():
    print(key, "->", val)

print("\n***********************************\n")
parts = [
    {"name": "R1", "ohms": 100},
    {"name": "R2", "ohms": 220},
    {"name": "R3", "ohms": 470},
]
print(parts[1]["name"])

print("\n***********************************\n")

text = "aabbbc"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)

print("\n***********************************\n")

parts = [
    {"name": "R1", "ohms": 100},
    {"name": "R2", "ohms": 220},
    {"name": "R3", "ohms": 470},
]

for p in parts:
    if p["ohms"] > 150:
        print(p["name"])
print([p["name"] for p in parts if p["ohms"] > 150])

print("\n***********************************\n")

ohms = [100, 220, 470, 1000]
currents_ma = [5 / r * 1000 for r in ohms]
print(currents_ma)

high_values = [r for r in ohms if r > 200]
print(high_values)

current_by_r = {r: round(5 / r * 1000, 2) for r in ohms}
print(current_by_r)

print({r % 100 for r in ohms})

pairs = [(a, b) for a in (100, 220) for b in (100, 220)]
print(pairs)

print("\n***********************************\n")

name_to_ohms = {p["name"]: p["ohms"] for p in parts}
print(name_to_ohms)

drops = [round(0.010 * p["ohms"], 2) for p in parts]
print(drops)
print("\n***********************************\n")

raw = """R1,100,0.25
R2,220,0.5
R3,470,0.25
R4,1000,0.125"""

parts = []
for line in raw.splitlines():
    name, ohms, watts = line.split(",")
    parts.append({"name": name, "ohms": int(ohms), "watts": float(watts)})

print(f"{'Name':<5} {'Ohms':>5} {'Watts':>6}")
for p in parts:
    print(f"{p['name']:<5} {p['ohms']:>5} {p['watts']:>6.2f}")
total = sum(p["ohms"] for p in parts)
print(f"Total series: {total} ohms")
