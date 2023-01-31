import math
from src.Figure import Figure

class Circle(Figure):
    def __init__(self, r):
        super().__init__("Circle")
        if r <= 0:
            raise ValueError
        s = math.pi * (r*r)
        self.area = math.sqrt(s)
        self.perimeter = r * math.pi * 2
