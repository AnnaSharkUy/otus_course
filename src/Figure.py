class Figure:
    def __init__(self, name):
        self.name = name
    
    @property
    def area(self):
        raise RuntimeError

    def add_area (self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
