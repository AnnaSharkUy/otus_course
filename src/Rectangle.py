import math
from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__("Rectangle")
        if a <= 0 or b <= 0:
            raise ValueError
        self._a = a
        self._b = b

    @property
    def area(self):
        return self._a * self._b

    @property
    def perimeter(self):
        return 2 * (self._a + self._b)
