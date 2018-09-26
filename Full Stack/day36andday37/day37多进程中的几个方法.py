# join()
import time
from multiprocessing import Process


def func(arg1, args2):
    print('*'*arg1)
    time.sleep(5)
    print('*'*args2)


if __name__ == '__main__':
    p = Process(target=func, args=(10, 20))
    p.start()
    print('ahahha')
    p.join()     # 是感知一个子进程的结束，将异步的程序改为同步
    print('--------Game over')