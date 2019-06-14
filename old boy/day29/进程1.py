#进程间通信应该考虑PIPE和QUEUE
from multiprocessing import Process
import time
start_time = time.time()
def f(name):
    # time.sleep(1)
    print("hello",name,time.ctime())

if __name__ =="__main__":
    p_list=[]
    for i in range(3):
        p = Process(target=f,args=('lxl',))
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()
    print("end")
    end_time = time.time()
    print(end_time-start_time)