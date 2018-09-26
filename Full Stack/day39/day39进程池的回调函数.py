# 回调函数
import os
from multiprocessing import Pool


def func(n):
    print('in func', os.getpid())
    return n * n


def func1(nn):
    print('in func1', os.getpid())
    print(nn)


if __name__ == '__main__':
    print('主进程：', os.getpid())
    p = Pool()
    for i in range(10):
        p.apply_async(func, args=(10, ), callback=func1)
    p.close()
    p.join()