d = {1:'raz',2:'geru',3:'20',4:'xyz'}
print("1st name is"+d[1])
print("2nd name is"+d[4])
print(d)
print(d.keys())
print(d.values())
print(len(d))
d.pop(3)
print(d)
print(d.clear())
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 5, 'c': 3}

if dict1 == dict2:
    print("Dictionaries are equal")
else:
    print("Dictionaries are not equal")

