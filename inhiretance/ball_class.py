from math import pi
from inhiretance.circle_class import Circle

class ball(Circle):

    def volume(self):
        volume = (3 / 4) * self.radius ** 3 * pi
        return volume

    def area(self):
        return self.radius ** 2 * pi

    def print_area(self):
        print("the area is " + str(super().area()))

# السوبر عشان ياخذ القيمه من الاب الي هي الدائره