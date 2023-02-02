import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        super().__init__("Circle")
        if r <= 0:
            raise ValueError
        self._radius = r

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    @property
    def perimeter(self):
        return self._radius * math.pi * 2
