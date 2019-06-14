#同步锁：数据安全
#用于很多线程同时取一个数据的情况
#
import time
import threading

def addNum():
    global num
    #num -=1
    print("ok")
    r.acquire()
    print(1)
    temp = num
    # time.sleep(1)
    num = temp-1
    r.release()

lock = threading.RLock()#递归锁 可重用的锁
r = threading.Lock()
num = 100

thread_list = []
for i in range(100):
    t = threading.Thread(target = addNum)
    t.start()
    thread_list.append(t)


# for t in thread_list:
#     t.join()

print('final num',num)