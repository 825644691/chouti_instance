import time
import threading


class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num = num

    def run(self):
        print('running on number %s' %self.num)
        time.sleep(3)


if __name__ == "__main__":
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
