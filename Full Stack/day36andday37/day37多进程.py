import os
import time
from multiprocessing import Process


def func(args):
    print(args)
    time.sleep(1)
    print('子进程: ', os.getpid())
    print('子进程的父进程: ', os.getppid())
    print(54321)


if __name__ == '__main__':
    p = Process(target=func, args=('餐宿',))
    # p是一个进程对象（C语言和操作系统做交互），还没启动
    p.start()     # 告诉操作系统，开启子进程
    print('*'*10)
    print('父进程: ', os.getpid())   # getpid查看当前进程的进程号
    print('父进程的父进程: ', os.getppid())


# 进程的生命周期
#     主进程
#     子进程
#     开启了子进程的主进程：
#         主进程自己的代码如果长，等待自己的代码执行结束
#         子进程的执行时间长，主进程会在主进程代码执行完毕之后等待子进程执行完毕之后，主进程才结束
