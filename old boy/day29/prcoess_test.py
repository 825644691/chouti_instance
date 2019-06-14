from multiprocessing import Process
import time


begin = time.time()
def add(n):
    for i in range(n):
        sm = 0
        sm +=i
    print(sm)


add(10000000)
add(20000000)


# p1 = Process(target=add,args=(10000000,))
# p2 = Process(target=add,args=(20000000,))
# p1.run()
# p2.run()
end = time.time()
print(end - begin)

