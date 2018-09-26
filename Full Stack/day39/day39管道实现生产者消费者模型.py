import time
import random
from multiprocessing import Pipe, Process, Lock


# def producer(conn, pro, name, food):
#     conn.close()
#     for i in range(20):
#         time.sleep(random.random())
#         f = '{} produce {} {}'.format(name, i, food)
#         print(f)
#         pro.send(f)
#     pro.close()
#
#
# def consumer(conn, pro, name):
#     pro.close()
#     while True:
#         try:
#             food = conn.recv()
#             print('{} eat {}'.format(name, food))
#             time.sleep(random.random())
#         except EOFError:
#             conn.close()
#             break
#
#
#
# if __name__ == '__main__':
#     conn, pro = Pipe()
#     lock = Lock()
#     p = Process(target=producer, args=(conn, pro, 'tomoya', 'sweet'))
#     p.start()
#     c = Process(target=consumer, args=(conn, pro, 'shigeko'))
#     c.start()
#     c1 = Process(target=consumer, args=(conn, pro, 'ani'))
#     c1.start()
#     conn.close()
#     pro.close()

# pipe，数据不安全性
# IPC
# 解决：加锁
# 加锁来控制操作管道的行为，来避免进程之间争抢数据不安全现象

def producer(conn, pro, n):
    conn.close()
    for i in range(n):
        pro.send(i)
    pro.send(None)
    pro.send(None)
    pro.close()


def consumer(conn, pro, name, lock):
    pro.close()
    while True:
        lock.acquire()
        bread = conn.recv()
        lock.release()
        if bread:
            print('{} get the bread: {}'.format(name, bread))
        else:
            conn.close()
            break


if __name__ == '__main__':
    conn, pro = Pipe()
    lock = Lock()
    p = Process(target=producer, args=(conn, pro, 30))
    p.start()
    c = Process(target=consumer, args=(conn, pro, 'shigeko', lock))
    c.start()
    c1 = Process(target=consumer, args=(conn, pro, 'ani', lock))
    c1.start()
    conn.close()
    pro.close()


# 队列，进程之间数据安全的
# 管道 + 锁