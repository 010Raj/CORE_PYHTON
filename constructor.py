'''class shape:
    def __init__(self, name):
        self.name = name

        def area(self):
            pass

        class rectangle(shape):
            def __init__(self, name, length, width):
                super().__init__(name)
                self.length = length
                self.width = width

            def area(self):
                return self.length * self.width

        class circle(shape):
            def __init__(self, name, radius):
                super().__init__(name)
                self.radius = radius

            def area(self):
                return 3.14 * (self.radius ** 2)

        class triangle(shape):
            def __init__(self, name, base, height):
                super().__init__(name)
                self.base = base
                self.height = height

            def area(self):
                return 0.5 * self.base * self.height

            rect = rectangle("rectangle", 4, 5)
            circle = circle("circle", 3)
            triangle = triangle("triangle", 5, 6)

            print(react.name, "area:", react.area())
            print(circle.name, "area:", circle.area())
            print(triangle.name, "area:", triangle.area())
            '''
'''
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

rect = Rectangle("Rectangle", 4, 5)
circle = Circle("Circle", 3)
triangle = Triangle("Triangle", 5, 6)

print(rect.name, "area:", rect.area())
print(circle.name, "area:", circle.area())
print(triangle.name, "area:", triangle.area())
'''
'''
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Shyam", "Pandey")
x.printname()
'''
'''
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)

x = student("raghav","goswami")
x.printname()
'''
#polymorphism
'''
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the primary language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of the U.S.A.")

    def language(self):
        print("English is the primary language of the U.S.A.")

    def type(self):
        print("U.S.A is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
'''
#Encapsulation
'''
class fruits:
    def __init__(self):
        self.price = 100
        self._bags = 5
    def display(self):
        print(self._bags)
obj=fruits()
obj.display()
'''


