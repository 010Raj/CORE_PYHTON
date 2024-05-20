'''
class Employee:
    'common base for all employees'
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displaycount(self):
        print("Total employees:", Employee.empcount)

    def displayemployee(self):
        print("Name:", self.name, "Salary:", self.salary)

emp1 = Employee("John", 50000)
emp2 = Employee("Alice", 60000)

emp1.displaycount()  # Output: Total employees: 2
emp1.displayemployee()  # Output: Name: John Salary: 50000
emp2.displayemployee()  # Output: Name: Alice Salary: 60000
'''

'''
# constructor usage using __init__ fun.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an instance of the Person class
person_obj = Person("Ram", 36)
print(person_obj.name)
print(person_obj.age)
'''

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("Hello, my name is " + self.name)

# Creating an instance of the Person class
p1 = Person("Ram", 36)
p1.myFunction()

'''

'''
# self parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello, my name is " + self.name)


p1 = Person("Ram", 36)
p1.my_function()
'''

'''
class person:
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

        person = person()
        p.set_name("anni")
        p.set_age(24)
        p.set_address("Indore")
        print(p.get_age(), p.get_name(), p.get_address())
       '''
'''
class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__address = ""

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

# Creating an instance of the Person class
p = Person()
p.set_name("Anni")
p.set_age(24)
p.set_address("Indore")
print(p.get_name(), p.get_age(), p.get_address())
'''


class car:
    def __init__(self):
        self.__carname = ""
        self.__version = ""
        self.__topspeed = 0
        self.__gears = 0
        self.__colour = ""


def get_carname(self):
    return self.__carname


def get_version(self):
    return self.__version


def get_topspeed(self):
    return self.__topspeed

def get_gears(self):
    return self.__gears

def get_colour(self):
    return self.__colour

def set_carname(self, carname):
    self.__name = carname

def set_version(self, version):
    self.__age = version

def set_topspeed(self, topspeed):
    self.__address = topspeed

def set_gears(self, gears):
    self.__name = gears

def set_colour(self, colour):
        self.__name = colour

c = car()
c.set_carname("supra")
c.set_version("Mk4")
c.set_topspeed(400)
c.set_gears(6)
c.set_colour("lime Green")
print(c.get_carname(), c.get_version(), c.get_topspeed(), c.get_gears(), c.get_colour())


