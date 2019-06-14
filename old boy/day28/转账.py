import threading
import time

class Account:
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def withdraw(self,num):
        time.sleep(1)
        self.money -= num

    def repay(self,num):
        self.money +=num


def transfer(_from,to,money):
    _from.withdraw(money)
    to.repay(money)

a1 = Account('LXL',1000)
a2 = Account('jx',500)

t1 = threading.Thread(target=transfer,args=(a1,a2,100))
t2 = threading.Thread(target=transfer,args=(a2,a1,100))
t1.start()
t1.join()
t2.start()
t2.join()
print(a1.money)
print(a2.money)

