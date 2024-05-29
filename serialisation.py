import pickle


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


p = Person("raj", "geru")
f = open("serialisation.txt", 'wb')
pickle.dump(p, f)
print("done")
f.close()

f = open("serialisation.txt", "rb")
p = pickle.load(f)
f.close()
print(p.fname,p.lname)

