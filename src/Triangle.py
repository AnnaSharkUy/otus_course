import math
from src.Figure import Figure

class Triangle(Figure):
    def __init__(self, a,b,c):
        super().__init__("Triangle")
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError
        self.perimeter = a + b + c
        p = self.perimeter / 2
        s = p*(p-a)*(p-b)*(p-c)
        self.area = math.sqrt(s)
