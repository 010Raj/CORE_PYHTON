import mod as RJ # yaha pe me "as" ka use  module ko rename karne ke liye de raha hu
RJ.greeting("python")
#dictionary updates
a = RJ.person["age"]
a1 = RJ.person["name"]
a2 = RJ.person["country"]

print(a)
print(a2)
print(a1)

import platform
x = platform.system()
print(x)

#here we are using dir() function to see what's in the directory
x = dir(platform)
print(x)

