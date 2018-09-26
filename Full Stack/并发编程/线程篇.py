# GIL
#     python(特指Cpython)的多线程的代码并不能利用多核的优势，而是通过著名的 "全局解释锁（GIL）"来处理。
# import time
# import threading
#
#
# def profile(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print('COST: {}'.format(end - start))
#     return wrapper
#
#
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# @profile
# def nothread():
#     fib(35)
#     fib(35)
#
#
# @profile
# def hasthread():
#     for i in range(2):
#         t = threading.Thread(target=fib, args=(35, ))
#         t.start()
#     main_thread = threading.currentThread()
#     for t in threading.enumerate():
#         if t is main_thread:
#             continue
#         t.join()
#
#
# nothread()
# hasthread()

# COST: 6.52224063873291
# COST: 6.57463526725769
# 由于电脑性能问题，所以在快慢方面并没过大的差距，但确实比多线程快
# GIL是必须的，Python解释器是非线程安全的。这就意味着当从线程内尝试安全的访问Python对象的时候将有一个全局的强制锁。
#


# --------------------同步机制----------------
#     Semaphore(信号量)
#         在线程编程中，为了防止不同的线程同时对一个供用的资源（比如全局变量）进行修改，需要进行同时访问的数量（通常是1）
#         信号量同步基于内部计数器：acquire()  release()，当计数器为0时，acquire()调用被阻塞
# import time
# from random import random
# from threading import Thread, Semaphore
#
#
# sema = Semaphore(3)
#
#
# def foo(tid):
#     with sema:
#         print('{} acquire sema'.format(tid))
#         time.sleep(random() * 2)
#     print('{} release sema'.format(tid))
#
#
# threads = []
#
#
# for i in range(5):
#     t = Thread(target=foo, args=(i, ))
#     t.start()
#     threads.append(t)
#
#
# for t in threads:
#     t.join()

# 结果：我们限制了同时能访问资源的数量为3
# 0 acquire sema
# 1 acquire sema
# 2 acquire sema
# 2 release sema
# 3 acquire sema
# 0 release sema
# 4 acquire sema
# 4 release sema
# 1 release sema
# 3 release sema


#     Lock(锁)
#         Lock也可以叫互斥锁，其实相当于信号量为1
# 不加锁例子：
# import time
# from threading import Thread
#
#
# value = 0
#
#
# def getlock():
#     global value
#     new = value + 1
#     time.sleep(0.001)  # 使用sleep让线程有机会切换
#     value = new
#
#
# threads = []
#
# for i in range(100):
#     t = Thread(target=getlock)
#     t.start()
#     threads.append(t)
#
#
# for t in threads:
#     t.join()
#
#
# print(value)

# 不加锁的情况下，结果会远远小于100
# 那加锁呢：
# import time
# from threading import Thread, Lock
#
# value = 0
# lock = Lock()
#
#
# def getLock():
#     global value
#     with lock:
#         new = value + 1
#         time.sleep(0.001)
#         value = new
#
#
# threads = []
#
#
# for i in range(100):
#     t = Thread(target=getLock)
#     t.start()
#     threads.append(t)
#
#
# for t in threads:
#     t.join()
#
# print(value)


#     RLock(可重入锁)
#         acquire()能够不被阻塞的被同一个线程调用多次。但是要注意的时release()需要调用与acquire()相同次数才能释放锁


#     Condition(条件)
#         一个线程等待特定条件，而另一个线程发出特定条件满足的信号。
#         最好的例子就是【生产者/消费者】模型
# import time
# import threading
#
#
# def consumer(cond):
#     t = threading.currentThread()
#     with cond:
#         cond.wait()  # wait()方法创建了一个名为waiter的锁，并且设置锁的状态为locked。这个waiter锁用于线程间的通讯
#         print('{}: Resource is available to consumer'.format(t.name))
#
#
# def producer(cond):
#     t = threading.currentThread()
#     with cond:
#         print('{}: Making resource available'.format(t.name))
#         cond.notifyAll()  # 释放waiter锁，唤醒消费者
#
#
# condition = threading.Condition()
#
# c1 = threading.Thread(name='c1', target=consumer, args=(condition, ))
# c2 = threading.Thread(name='c2', target=consumer, args=(condition, ))
# p = threading.Thread(name='p', target=producer, args=(condition, ))
#
# c1.start()
# time.sleep(1)
# c2.start()
# time.sleep(1)
# p.start()


#     Eevent(事件)
#        一个线程发送/传递事件，另外的线程等待事件的触发。
# import time
# import threading
# from random import randint
#
#
# TIMEOUT = 2
#
#
# def consumer(event, l):
#     t = threading.currentThread()
#     while True:
#         event_is_set = event.wait(TIMEOUT)
#         if event_is_set:
#             try:
#                 integer = l.pop()
#                 print('{} popped from list by {}'.format(integer, t.name))
#                 event.clear()  # 重置事件状态
#             except IndexError:  # 为了让刚启动时容错
#                 pass
#
#
# def producer(event, l):
#     t = threading.currentThread()
#     while True:
#         integer = randint(10, 100)
#         l.append(integer)
#         print('{} appended to list by {}'.format(integer, t.name))
#         event.set()  # 设置事件
#         time.sleep(1)
#
#
# event = threading.Event()
# l = []
#
# threads = []
#
# for name in ('consumer1', 'consumer2'):
#     t = threading.Thread(name=name, target=consumer, args=(event, l))
#     t.start()
#     threads.append(t)
#
#
# p = threading.Thread(name='producer1', target=producer, args=(event, l))
# p.start()
# threads.append(p)
#
# for t in threads:
#     t.join()


# 结果事件被2个消费者比较平均的接收并处理了。如果使用wait方法，线程就会等待我们设置事件，这也有助于保证任务的完成。


#     Queue(队列)
#         队列在并发开发中最常用的。我们借助【生产者/消费者】模式来理解：生产者把生产的【消息】放入队列，消费者从这个队列中对去对应的消息执行
#         主要关心如下4个方法就好：
#             1.put:向队列中添加一个项
#             2.get:从队列中删除并返回一个项
#             3.task_done:当某一项任务完成时调用
#             4.join:阻塞直到所有的项目都被处理完
# import time
# import threading
# from random import random
# from queue import Queue
#
# q = Queue()
#
#
# def double(n):
#     return n * 2
#
#
# def producer():
#     while True:
#         wt = random()
#         time.sleep(wt)
#         q.put((double, wt))
#
#
# def consumer():
#     while True:
#         task, arg = q.get()
#         print(arg, task(arg))
#         q.task_done()
#
#
# for target in (producer, consumer):
#     t = threading.Thread(target=target)
#     t.start()

# 以上就是最简化的队列架构

# Queue模块还自带了PriorityQueue（带有优先级）和LifoQueue（后进先出）2种特殊队列。
# 我们这里展示下线程安全的优先级队列的用法，
# PriorityQueue要求我们put的数据的格式是(priority_number, data)
# import time
# import threading
# from random import randint
# from queue import PriorityQueue
#
# q = PriorityQueue()
#
#
# def double(n):
#     return n * 2
#
#
# def producer():
#     count = 0
#     while True:
#         if count > 5:
#             break
#         pri = randint(0, 100)
#         print('put:{}'.format(pri))
#         q.put((pri, double, pri))  # (priority, func, args)
#         count += 1
#
#
# def consumer():
#     while True:
#         if q.empty():
#             break
#         pri, task, arg = q.get()
#         print('[PRI:{}] {} * 2 = {}'.format(pri, arg, task(arg)))
#         q.task_done()
#         time.sleep(0.1)
#
#
# t = threading.Thread(target=producer)
# t.start()
# time.sleep(1)
# t = threading.Thread(target=consumer)
# t.start()

# 可以看到put时的数字是随机的，但是get的时候先从优先级更高（数字小表示优先级高）开始获取的。



# 线程池

# 面向对象开发中，创建和销毁对象是很费时的，因为创建一个对象要获取内存资源或其他跟多资源。
# 如果创建一个线程池，一方面可以控制同时工作的线程数量，一方面也避免了创建和销毁产生的开销

# from multiprocessing.pool import ThreadPool
#
#
# pool = ThreadPool(5)
# ret = pool.map(lambda x: x ** 2, range(5))
# print(ret)

# 或自己实现一个:
import time
import threading
from random import random
from queue import Queue


def double(n):
    return n * 2


class Worker(threading.Thread):

    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()

    def run(self):
        while True:
            f, args, kwargs = self._q.get()
            try:
                print('USE: {}'.format(self.name))  # 线程名字
                print(f(*args, **kwargs))
            except Exception as e:
                print(e)
            self._q.task_done()


class ThreadPool(object):

    def __init__(self, num_t = 5):
        self._q = Queue(num_t)
        # Create worker Thread
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()


pool = ThreadPool()
for _ in range(8):
    wt = random()
    pool.add_task(double, wt)
    time.sleep(wt)
pool.wait_complete()

# 线程池会保证同时提供5个线程工作，但是我们8个待完成的任务，可以看到线程按顺序被循环利用了