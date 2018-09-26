import time
from threading import Thread


def func():
    while True:
        print('*'*10)
        time.sleep(1)


def func1():
    print('in func1')
    time.sleep(5)


t = Thread(target=func)
t.daemon = True   # 主线程结束，守护线程随之结束
t.start()
t1 = Thread(target=func1)
t1.start()
t1.join()
print('主线程')

# 守护进程随着主进程代码的执行结束而结束
# 守护线程会在住线程结束之后等待其他子线程的结束才结束

# 主进程在执行完自己的代码之后不会立即结束，而是等待子进程结束之后，回收子进程的资源
# import time
# from multiprocessing import Process
#
#
# def func():
#     time.sleep(5)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()