from time import sleep
from threading import *
import threading


class Account:
    balance = 0

    def __init__(self):
        self.lock = threading.Lock()

    def get_balance(self):
        sleep(2)
        return self.balance

    def set_balance(self, amount):
        sleep(2)
        self.balance(self, amount)

    def deposit(self, amount):
        self.lock.acquire()
        bal = self.get_balnce()
        self.lock.release()


class Racing(Thread):
    account: Account
    name = "no name"

    def __init__(self, account, name):
        super(Racing, self).__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposit(100)
        print(self.name, self.account.get_balance())

def main_task():
    acc = Account()

    t1 = Racing(acc, "ram")
    t2 = Racing(acc, "shyam")

    t1.start()
    t2.start()

    t1.Join()
    t2.Join()
    print("finish")

main_task()
