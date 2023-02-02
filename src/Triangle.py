import math
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError
        self._a = a
        self._b = b
        self._c = c

    @property
    def perimeter(self):
        return self._a + self._b + self._c

    @property
    def area(self):
        p = self.perimeter / 2
        s = p * (p - self._a) * (p - self._b) * (p - self._c)
        return math.sqrt(s)
