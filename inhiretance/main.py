from inhiretance.ball_class import ball # to appear this sentence clik alt & enter
from inhiretance.cylinder_class import cylinder

'''
b_1 = ball(1)
print(b_1.volume())'''

b_1 = ball(1)
b_1.print_area()


cy = cylinder(3,5)
print("the area is " + str(cy.area()))
print("the circumference is " + str(cy.circumference()))
print("the area is " + str(cy.area_of_base().area()))