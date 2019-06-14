import time
import threading
#一个线程就是一个指令机
#IO密集型任务或函数
#计算密集型任务或者函数
#python不能并行，因为cpython解析器有GIL的原因，全局解析器锁
#在同一时刻，只有一个线程进入解析器
#thread.join()阻塞



def foo(n):
    print("foo%s" %n)
    time.sleep(1)

def bar(n):
    print('bar%s' %n)
    time.sleep(2)

t1 = threading.Thread(target = foo,args = (1,))
t2 = threading.Thread(target = bar,args = (2,))
t1.start()
t2.start()

print("=============in the main==============")