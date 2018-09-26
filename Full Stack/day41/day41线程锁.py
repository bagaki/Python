import time
from threading import Lock, Thread

# Lock是互斥锁

#
# def eat1(lock):
#     global n
#     lock.acquire()
#     temp = n
#     time.sleep(0.2)
#     n = temp - 1
#     lock.release()
#
# n = 10
# t_lst = []
# lock = Lock()
# for i in range(10):
#     t = Thread(target=eat1, args=(lock, ))
#     t.start()
#     t_lst.append(t)
#
# for t in t_lst:
#     t.join()
# print(n)


# 科学家吃面

# noodle_lock = Lock()
# fork_lock = Lock()
# def eat(name):
#     noodle_lock.acquire()
#     print('{} Get the noodle'.format(name))
#     fork_lock.acquire()
#     print('{} Get the fork'.format(name))
#     print('{} Eat the noodle'.format(name))
#     fork_lock.release()
#     noodle_lock.release()
#
#
# def eat1(name):
#     fork_lock.acquire()
#     print('{} Get the fork'.format(name))
#     time.sleep(1)
#     noodle_lock.acquire()
#     print('{} Get the noodle'.format(name))
#     print('{} Eat the noodle'.format(name))
#     noodle_lock.release()
#     fork_lock.release()
#
#
# t = Thread(target=eat, args=('bagaki', ))
# t.start()
# t1 = Thread(target=eat1, args=('tomoya', ))
# t1.start()
# t2 = Thread(target=eat, args=('shigeko', ))
# t2.start()

from threading import RLock  # 递归锁，为了解决死锁问题

noodle_lock = fork_lock = RLock()  # 一个钥匙串上的两把钥匙

def eat(name):
    noodle_lock.acquire()
    print('{} Get the noodle'.format(name))
    fork_lock.acquire()
    print('{} Get the fork'.format(name))
    print('{} Eat the noodle'.format(name))
    fork_lock.release()
    noodle_lock.release()


def eat1(name):
    fork_lock.acquire()
    print('{} Get the fork'.format(name))
    time.sleep(1)
    noodle_lock.acquire()
    print('{} Get the noodle'.format(name))
    print('{} Eat the noodle'.format(name))
    noodle_lock.release()
    fork_lock.release()


t = Thread(target=eat, args=('bagaki', ))
t.start()
t1 = Thread(target=eat1, args=('tomoya', ))
t1.start()
t2 = Thread(target=eat, args=('shigeko', ))
t2.start()