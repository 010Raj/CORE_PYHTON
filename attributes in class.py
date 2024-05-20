class shape:
    '''name = "Circle"#set an attribute for 'name' of the class
    #instantate the class snake and assign it to variable snake'''


# Python code for accessing methods using static method
class Shape:

    name = 'abc'

    def circleArea(radius):
        area = (22 * radius * radius) / 7
        print('circle area = ', area)

    def reactangleArea(length, width):
        area = length * width
        print('reactangle area = ', area)

    def sum(a, b):
        total = a + b
        print('sum = ', total)


shape = Shape()
print(shape.name)
Shape.circleArea(20)
Shape.sum(10, 20)
Shape.reactangleArea(10, 20)



