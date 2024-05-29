'''
file = open("C:/Users/hp/Desktop/IO/raj.txt", 'w')
file.write("hey there! ,you are welcome to my workspace \n")
file.write(". File I/O \n")
file.write("Python too supports file handling and allows users to handle files i.e., to read and write files, along \n")
file.write("with many other file handling options, to operate on files. The concept of file handling has \n")
file.write("stretched over various other languages, but the implementation is either complicated or lengthy,\n")
file.write("but a like other concepts of Python, this concept here is also easy and short. Python treats file \n")
file.write("differently as text or binary and this is important. Each line of code includes a sequence of \n")
file.write("characters and they form text file. Each line of a file is terminated with a special character, called \n")
file.write("the EOL or End of Line characters like comma {,} or newline character. It ends the current line \n")
file.write("and tells the interpreter a new one has begun \n")
print(type(file))
print("done")
file.close()
'''
# import fileinput

'''
file =open("mymodule.py", 'w')
file.write("hie watsssup guys!!!")
file.close()
'''
'''
def readfile():
    file = open("mymodule.py")
    text = file.read()  # it will read all data
    print(text)
    file.close()
    return
'''
'''
#read a file specific parts
fo = open("C:/Users/hp/Desktop/IO/raj.txt", 'r')
print("file name : ",fo.name)
print("mode of opening : ",fo.mode)
print("is closed",fo.closed)
fo.close()
'''
'''
# it reads the complete file
file = open("C:/Users/hp/Desktop/IO/raj.txt")
text = file.read()
print(text)
print(type(text))
file.close()
'''
'''
#it reads the line of a file
file = open("C:/Users/hp/Desktop/IO/raj.txt")
for line in file:
    print(line)
'''
'''
# with open
with open("C:/Users/hp/Desktop/IO/raj.txt", 'w')as file:
    file.write("hello here is a file by using with a statement \n")
    file.write("that is a text file")
    print("done")
'''
