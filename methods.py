'''class shape:
    name = "circle"

    def change_name(self,new_name):
        self.name = new_name
    shape_obj = shape()
    print(shape_obj.name)
    shape.change_name("triangle")
    print(shape_obj  .name)'''
'''class employee:
    'common base class fore all employees'
    empcount = 0
    def __init__(self, name , salary ):
        self.name = name
        self.salary = salary
        employee.empcount += 1
        def displaycount (self):
            print ("total employees %d" % employee.empcount)
            def displayemployee(self):
                print("name : ", self.name, "salary : ", self.salary)

'''


class employee:
    'common base class for all employees'
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empcount += 1

    def displaycount(self):
        print("Total employees: %d" % employee.empcount)

    def displayemployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
    