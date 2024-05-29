#List Example
a = [5,10,15,20,25,30,35,40]
print("a[2] = ", a[2])
print("a[-3] = ", a[-3])

#Example of string
str1 = 'नमस्ते राज,\n'
str2 = ' भाई, तुम कैसे हो? \n'
print (str1[0:2])
print (str1[8])
print (str1 * 2)
print (str1 + str2)

#Example of dictionary
dictionary_list = {1:'Ram', 2:'Shyam', 3:'Balram', 4:'Raju'};
print("1st name is "+dictionary_list[1]);
print("2nd name is "+ dictionary_list[4]);
print (dictionary_list);
print (dictionary_list.keys());
print (dictionary_list.values());

#creating tuple
my_tuple = ()
print(my_tuple)

tuple_list1 = (1, 2.8, "Hello Raj")
print(tuple_list1)

tuple_list2 = ("किताब", [1, 2, 3])
print(tuple_list2)

tuple_list4 = (1, "बालवीर", (11, 22, 33))

print(tuple_list4[1][2])
print(tuple_list4[2][2])

# calculate age
from datetime import date


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

'''
year = int(input("अपना जन्म वर्ष दर्ज करें = "))
month = int(input("अपना जन्म माह दर्ज करें = "))
day = int(input("अपना जन्म दिन दर्ज करें = "))
age = calculateAge(date(year, month, day))
print(age, "साल")
'''
#current year
from datetime import date,timedelta
currentStatus= date.today()
print("आज की तारीख =", currentStatus.day)
print("अभी चल रहा माह=", currentStatus.month)
print("चालू वर्ष =", currentStatus.year)

#check tomorrow Date
tomorrowDate=currentStatus+timedelta(days=1)
print("कल की तारीख = ",tomorrowDate)

aftertomorrow=tomorrowDate+timedelta(days=1)
print("कल के बाद की तारीख = ",aftertomorrow)

previousDate=currentStatus-timedelta(days=1)
print("पिछली तिथि = ",previousDate)

#for loop
numbers = [1, 2, 4, 6, 11, 20]

for val in numbers:
    square = val * val
    print(square)

#if else
price = 99.9
if (price < 100.0):
        print("उफ़, मैं यह पिज़्ज़ा नहीं खरीद सकता")
        print("मैं पिज्जा नहीं मिलने के कारण रो रहा हूं, हे प्रभु आहे हरि राम कृष्ण जगन्नाथ पेमनदी ये क्या हुआ")
else :
        print("हाँ, आख़िरकार मैं पिज़्ज़ा खरीद सकता हूँ")
        print("यम यम आपका पिज़्ज़ा बहुत स्वादिष्ट है :)")

#nested if else

age = int(input(" कृपया यहां अपनी आयु दर्ज करें :  "))
if age < 18:
    print(" मेरे बच्चे, तुम इसके लिए बहुत छोटे हो  ")
    print("मेरे बच्चे, मुझे यकीन है कि वह दिन आएगा जब तुम एक पुरुष बन जाओगे ")
else:
    if age >= 18 and age <= 60:
        print("आप काम करने के योग्य हैं ")
        print("कृपया अपना विवरण भरें और आवेदन करें")
    else:
        print(" सच में लानत है लड़के तुम दादा बनने के योग्य हो, तुम सरकारी नियमों के अनुसार काम करने के लिए बहुत बूढ़े हो गए हो ")
        print(" कृपया अपनी पेंशन लीजिए! और वृद्धाश्रम चले जाओ")

# arithmetic operators
num1 = 10
num2 = 20
print("Num1 + Num2=", num1 + num2)
print("Num1 - Num2=", num1 - num2)
print("Num1 * Num2=", num1 * num2)
print("Num1 / Num2=", num1 / num2)
print("5^3=",5**3)
print("20%3=",20%3)
print("22/7=",22//7)

# assignment operators
x = 55
x *= 33
print(x)

# comparison operators
num1 = 911
num2 = 100
num3 = 108
print("Is Num3 > Num2=", num3 > num2)
print("Is Num2 =  Num3=", num3 == num2)
print("Is Num1 != Num2", num1!= num2)

# identiy operators
x = ["नारंगी", "शराब"]
y = ["नारंगी", "शराब"]
z = x
print(x is z)
print(x is y)
print(x == y)

#logical operators
x=True
y=False
print("X and Y",x and y)
print("X or Y",x or y)
print("Not of X",not x)

# Example of Python Functions using def keyword
#Function definition

def sum( a,b ):
   "It sum of two numbers"
   print('a',a,'b',b)
   c = a + b
   return c;

print(sum(5,10))
print(sum(10,20))

#keyword argument
d = sum(b=7,a=8)

#Pass by reference
def chageList( list ):
   list.append(6);
   print (list)
   return

list = [1,2,3,4,5]
print(list)
chageList(list)
print(list)

#Variable length
def sumnum( a, *varg ):
   t = a
   for n in varg:
      t+=n
   return t;

total = sumnum(1,2,3,4,5)
print('Total', total)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(fname):
  print(fname + " Gupta")

my_function("John")
my_function("Amy")
my_function("Linus")


#passing a List as parameter

print("Output show passing value as a parameter : ")
def my_function(food):
 for x in food:
   print(x)
fruits = ["Ram", "Shyam", "Jerry"]
my_function(fruits)

#Return value as parameter

print("Ouput show Return value as Parameter are : ")
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
