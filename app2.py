'''
class car :
    def __init__(self):
        print("new car")
    name = ""
    cylinder = ""
    color = ""
    price = 9000
    model=2011

x = car()
x.price = 5000
x.color = "red"
x.name = "accent"
x.cylinder= 4
x.model = 2015

b = car()
b.price = 15000
b.color = "blue"
b.name = "toyota"
b.cylinder= 3
b.model = 2010

ff = car()
ff.price = 15000
ff.color = "blue"
ff.name = "toyota"
ff.cylinder= 3
ff.model = 2010

print(ff.model)
print(x.model)
print(b.name)


class car :
    name = ""
    cylinder = ""
    color = ""
    price = 9000
    model=2011

    def __init__(self,name, cylinder ,color ,price ,model):
        print("new car")
        self.name = name
        self.cylinder =cylinder
        self.color =color
        self.price = price
        self.model=model


x = car( "toyota",15000,"blue",3, 2010)
b = car( "merc",19000,"red",7, 2009)

print(x.model)
print(b.color)

class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area= self.radius **2 * 3.14
        return area
    def circumference(self):
        circumference= self.radius * 2 * 3.14
        return circumference

c1= circle(5)
c2= circle(10)
print(c1.area())

c1= circle(5)
c2= circle(10)
print(c1.circumference())
print(c2.circumference())''' 