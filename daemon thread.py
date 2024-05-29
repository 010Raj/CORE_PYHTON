import threading
import time

def first_thread():
    print('Hello Raj')
    time.sleep(10)
    print('Bye Raj')

def second_thread():
    print('Hello Rohit')
    time.sleep(10)
    print('Bye Rohit')

# Correct the case for `True`
t1 = threading.Thread(target=first_thread, daemon=True)
t2 = threading.Thread(target=second_thread)

t1.start()
t2.start()

# Join the non-daemon thread to ensure the main program waits for it to finish
t2.join()
