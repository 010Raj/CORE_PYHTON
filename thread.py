# Hello without thread
import threading
from threading import *
def hello():
    for i in range(15):
        print("hello", i)

    def hi():
        for i in range(15):
            print("hi", i)

        # multithreading

t1 = threading.thread(target1=hello)
t2 = threading.thread(target2=hi)
# start threads
t1.start()
t2.start()
