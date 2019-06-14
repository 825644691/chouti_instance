import threading
from random import randint
import time
# threading.Condition.wait()有两个作用，释放和等待
# threading.Condition.notify()把wait()激活一个对象
#进程间通信

class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(0,100)
            print('生产者',self.name,":Append"+str(val),L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()
            if len(L) ==0:
                lock_con.wait()
            print('消费者',self.name,":Delete"+str(L[0]),L)
            del L[0]
            lock_con.release()
            time.sleep(1)




if __name__ =="__main__":
    L=[]
    lock_con = threading.Condition()#创建条件变量锁
    threads = []
    threads.append(Consumer())
    for i in range(5):

        threads.append(Producer())

    for t in threads:
        t.start()
    for t in threads:
        t.join()