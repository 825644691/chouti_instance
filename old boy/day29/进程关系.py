from multiprocessing import Process
import os
import time
#os.getppid:获取父进程号
#os.getpid:获取进程号


def info(title):
    print(title)
    print('module name',__name__)
    print('parent process',os.getppid())
    print('process id',os.getpid())


if __name__ == "__main__":
    info('\033[32;1mmain process line\033[0m')
    time.sleep(3)
    p = Process(target=info,args=('bob',))
    p.start()
    p.join()