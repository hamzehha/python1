from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius ** 2 * pi
        return area

    def circumference(self):
        circumference = self.radius * 2 * pi
        return circumference


