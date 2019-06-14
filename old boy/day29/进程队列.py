import queue

# queue.Queue()创建的是一个线程队列
#from multiprocessing import Queue创建一个进程队列

from multiprocessing import Process,Queue

def f(q):
    q.put([42,2,'hello'])
    print(id(q))
    

if __name__ == "__main__":
    q = Queue()
    print(id(q))
    p_list = []
    for i in range(3):
        p = Process(target=f,args=(q,))
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    for i in p_list:
        i.join()