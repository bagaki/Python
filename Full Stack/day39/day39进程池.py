# 为什么会有进程池的概念
#     效率
#     每开启进程，开启属于这个进程的内存空间
#     寄存器 堆栈 文件
#     进程过多 操作系统的调度

# 进程池
#     python中的进程池，先创建一个属于进程的池子
#     这个池子指定能存放多少个进程
#     先将这些进程创建好
# 更高级的进程池
#     n, m
#     三个进程

import time
from multiprocessing import Pool, Process


def func(n):
    for i in range(10):
        print(n+1)


if __name__ == '__main__':
    start = time.time()
    pool = Pool(3)
    pool.map(func, range(100))
    t1 = time.time() - start

    start1 = time.time()
    p_lst = []
    for i in range(100):
        p = Process(target=func, args=(i, ))
        p_lst.append(p)
        p.start()
    for p in p_lst:
        p.join()
    t2 = time.time() - start1
    print(t1, t2)