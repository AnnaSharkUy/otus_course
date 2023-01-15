import math
from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__("Rectangle")
        if a <= 0 or b <= 0:
            raise ValueError
        self.area = a * b
        self.perimeter = 2 * (a + b)