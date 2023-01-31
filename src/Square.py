import math
from src.Figure import Figure

class Square(Figure):
    def __init__(self, a):
        super().__init__("Square")
        if a <= 0:
            raise ValueError
        self.area = a * a
        self.perimeter = a * 4
