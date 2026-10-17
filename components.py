from math import pi


class Component:
    def __init__(self, name: str):
        self.name = name

    def impedance(self, freq: float) -> complex:
        raise NotImplementedError("Subclasses must implement impedance()")


class Resistor(Component):
    def __init__(self, name: str, ohms: float, watts: float = 0.25):
        super().__init__(name)
        self.ohms = ohms
        self.watts = watts

    def impedance(self, freq: float) -> complex:
        return complex(self.ohms, 0)

    @property
    def ohms(self) -> float:
        return self._ohms

    @ohms.setter
    def ohms(self, value: float):
        if value <= 0:
            raise ValueError(f"Resistance must be positive, got {value}")
        self._ohms = value

    def current(self, voltage: float) -> float:
        return voltage / self.ohms

    def power(self, voltage: float) -> float:
        return voltage * self.current(voltage)

    def is_overloaded(self, voltage: float) -> bool:
        return self.power(voltage) > self.watts

    def __repr__(self) -> str:
        return f"Resistor({self.name!r}, {self.ohms}, watts={self.watts})"

    def __eq__(self, other):
        if not isinstance(other, Resistor):
            return NotImplemented
        return self.ohms == other.ohms and self.watts == other.watts

    def __lt__(self, other):
        return self.ohms < other.ohms


class Capacitor(Component):
    def __init__(self, name: str, farads: float):
        super().__init__(name)
        self.farads = farads

    def impedance(self, freq: float) -> complex:
        return 1 / (2j * pi * freq * self.farads)

    def __repr__(self) -> str:
        return f"Capacitor({self.name!r}, {self.farads})"


class Inductor(Component):
    def __init__(self, name: str, henries: float):
        super().__init__(name)
        self.henries = henries

    def impedance(self, freq: float) -> complex:
        return 2j * pi * freq * self.henries

    def __repr__(self) -> str:
        return f"Inductor({self.name!r}, {self.henries})"


class Circuit:
    def __init__(self, components=None):
        self.components = list(components) if components else []

    def add(self, component: Component) -> None:
        self.components.append(component)

    def series_impedance(self, freq: float) -> complex:
        return sum(c.impedance(freq) for c in self.components)

    def parallel_impedance(self, freq: float) -> complex:
        if not self.components:
            raise ValueError("Circuit has no components")
        return 1 / sum(c.impedance(freq) for c in self.components)

    def rc_lowpass_gain(self, freq: float) -> float:
        resistors = [c for c in self.components if isinstance(c, Resistor)]
        capacitors = [c for c in self.components if isinstance(c, Capacitor)]
        if len(resistors) != 1 or len(capacitors) != 1:
            raise ValueError(
                "Circuit must contain exactly one resistor and one capacitor"
            )
        zr = resistors[0].impedance(freq)
        zc = capacitors[0].impedance(freq)
        return abs(zc / (zr + zc))

    def __len__(self) -> int:
        return len(self.components)
