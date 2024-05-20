'''
# Exception Handling:
a = 4
b = 0
try:
    c = a / b  # exception is created
    print(c)
except ArithmeticError as e:  # exception message
    print(e)
else:
    print("your division is greater than zero")
finally:      #finally can be used in both conditions wether its true or false,it does'nt matter this "finally" or affect
    print("this block will always be executed")
'''
'''
#raise exception
try:
    number = int (input("enter your number here: "))
    if number>10:
        raise Exception('Invalid number')
except Exception as e:
    print(e)
'''
'''
#Name Error
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
'''


