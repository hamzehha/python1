from math import pi

from inhiretance.circle_class import Circle


class cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return self.radius ** 2 * pi * self.height  # to appear this sentence clik alt & enter

    def area(self):
        return self.circ() * self.height

    def get_base(self):
        return super()

    def area_of_base(self):
        return super().area()
    # بترجع الدائره ومن الدائره بس المساحه
