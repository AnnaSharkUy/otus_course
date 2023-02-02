import math
from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__("Square")
        if a <= 0:
            raise ValueError
        self._a = a

    @property
    def area(self):
        return self._a * self._a

    @property
    def perimeter(self):
        return self._a * 4
