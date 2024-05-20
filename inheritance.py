#inheritance
##single level inheritance
'''
class parent:
    def show(self):
        print("parent method called")

class child(parent):
    def display(self):
        print("child method called")

obj = child()
obj.display()
obj.show()
'''
'''
##multilevel level inheritance
class grandparent:
    def show(self):
        print("Grandparent method called")

class parent(grandparent):
    def display(self):
        print("parent method called")

class child(parent):
    def show_child(self):
        print("child method called")

obj = child()
obj.show_child()
obj.display()
obj.show()
'''
#harirchial inheritance
'''
class parent:
    def show(self):
        print("parent method called")

class child1(parent):
    def display1(self):
        print("child 1 method called")

class child2(parent):
    def display2(self):
        print("child2 method is called")

obj1 = child1()
obj2 = child2()
obj1.display1()
obj1.show()
obj2.display2()
obj2.show()
'''
#mulpile inheritance
'''
class parent1:

    def show1(self):
        print("parent1 method called")

class parent2:

    def show2(self):
        print("parent2 method called")

class child(parent1,parent2):

    def display(self):
        print("child method called")

obj = child()
obj.display()
obj.show1()
obj.show2()
'''

#abstraction
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Instantiate objects
rect = Rectangle(4, 5)
circle = Circle(3)
triangle = Triangle(5, 6)

# Calculate and print areas
print("Area of rectangle:", rect.area())
print("Area of circle:", circle.area())
print("Area of triangle:", triangle.area())
'''
'''
from abc import ABC, abstractmethod
class polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class triangle(polygon):
    def noofsides(self):
        print("I have 3 sides")

class pentagon(polygon):
    def noofsides(self):
        print("I have 4 sides")

class hexagon(polygon):
    def noofsides(self):
        print("I have 5 slides")

class hexagon(polygon):
    def noofsides(self):
        print("I have 6 sides")

class quadilateral(polygon):
    def noofsides(self):
        print("I have 4 sides")

tri_obj = triangle
tri_obj.noofsides()
qua_obj = quadilateral()
qua_obj.noofsides()
penta_obj = pentagon()
penta_obj.noofsides()
hexa_obj = hexagon()
penta_obj.noofsides()
'''

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        return 3

class Quadrilateral(Polygon):
    def noofsides(self):
        return 4

class Pentagon(Polygon):
    def noofsides(self):
        return 5

class Hexagon(Polygon):
    def noofsides(self):
        return 6

tri_obj = Triangle()
print("Number of sides in triangle:", tri_obj.noofsides())

qua_obj = Quadrilateral()
print("Number of sides in quadrilateral:", qua_obj.noofsides())

penta_obj = Pentagon()
print("Number of sides in pentagon:", penta_obj.noofsides())

hexa_obj = Hexagon()
print("Number of sides in hexagon:", hexa_obj.noofsides())
