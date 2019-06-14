import threading


class Account:
    def __init__(self):
        self.r = threading.RLock()

a1 = Account()
print(a1.r)
a2 = Account()
print(a2.r)