import threading
import time

#Event 不是一把锁，但线程间可以通信
#Event.isSet()返回event的状态值
# threading.Event().wait()判断event.isSet()==False,如果True就等待，false就进去运行
# threading.Event().set()设置event的状态值为True，激活阻塞池的所有线程
# threading.Event().set()恢复event的状态池为True
class Boss(threading.Thread):
    def run(self):
        print("Boss:今晚大家都要加班到22：00")
        event.isSet() or event.set()
        # time.sleep(5)
        print("BOSS:<22:00>可以下班了")
        event.isSet() or event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("worker:哎，命苦啊")
        # time.sleep(0.25)
        event.clear()
        event.wait()
        print("worker:OhYeah!")

if __name__ =="__main__":
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()