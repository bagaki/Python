import os
import time
from multiprocessing import Pool


def func(n):
    print('start func {}'.format(n), os.getpid())
    time.sleep(1)
    print('end func {}'.format(n), os.getpid())


if __name__ == '__main__':
    p = Pool()
    for i in range(10):
        p.apply_async(func, args=(i, ))
    p.close()   # 结束进程池接收任务
    p.join()   # 感知进程中的任务执行结束