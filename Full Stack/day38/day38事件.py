# 通过一个信号，来控制 多个进程，同时执行或阻塞
# 事件

import time
import random
from multiprocessing import Event, Process


# 一个信号可以使所有的进程都进入阻塞状态
# 也可以控制所有的进程解除阻塞
# 一个事件被创建之后，默认使阻塞状态
# e = Event()   # 创建一个事件
# print(e.is_set())    # 查看一个事件的状态,状态默认被设置成阻塞
# e.set()              # 将这个事件的状态改为True
# print(e.is_set())
# e.wait()             # 是依据e.is_set()的值来决定是否阻塞的
# print(123456)
# e.clear()            # 将这个事件的状态改为False
# print(e.is_set())
# e.wait()
# print('***')


# set和clear
#     分别用来修改一个事件的状态 True or False
# is_set 用来查看一个事件的状态
# wait  是依据事件的状态来决定自己是否阻塞
#       False阻塞 True不阻塞


# 红绿灯事件
def car(e, i):
    if not e.is_set():
        print('car {} is waitting'.format(i))
        e.wait()   # 阻塞，知道得到一个事件状态编程True的信号
    print('\033[0;32;40mcar {} is pass\033[0m'.format(i))


def traffic_light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)




if __name__ == '__main__':
    e = Event()
    p = Process(target=traffic_light, args=(e, ))
    p.start()
    for i in range(20):
        cars = Process(target=car, args=(e,i))
        cars.start()
        time.sleep(random.random())