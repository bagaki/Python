# 进程：启动多个进程，进程之间是由操作系统负责调用
# 线程：启动多个线程，真正被CPU执行的最小单位实际是线程
#     开启一个线程，创建一个线程，寄存器，堆栈
# 协程
#     本质上是一个线程
#     能够在多个任务之间切换来节省一些IO时间
#     协程中任务之间的切换也消耗时间，但开销要远远小于进程线程之间的切换
# 实现并发的手段
from gevent import monkey;monkey.patch_all()
import time
import gevent
import requests
import threading
from greenlet import greenlet


# def consumer():
#     while True:
#         x = yield
#         time.sleep(1)
#         print('处理了数据', x)
#
#
# def producer():
#     c = consumer()
#     next(c)
#     for i in range(10):
#         time.sleep(1)
#         print('生产了数据',i)
#         c.send(1)
#
#
# producer()

# 真正的协程模块就是使用greenlet完成得分切换
# def eat():
#     print('eating start')
#     g2.switch()
#     print('eating end')
#     g2.switch()
#
#
# def play():
#     print('playing start')
#     g1.switch()
#     print('play end')
#
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
# g1.switch()


# def eat():
#     print(threading.current_thread().getName())
#     print(threading.current_thread())
#     print('eating start')
#     time.sleep(1)
#     print('eating end')
#
#
# def play():
#     print(threading.current_thread().getName())
#     print(threading.current_thread())
#     print('playing start')
#     time.sleep(1)
#     print('play end')
#
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# g1.join()
# g2.join()

# 进程和线程的任务切换由操作系统完成
# 协程任务之间的切换由程序完成，只有遇到协程模块能识别的IO操作的时候，程序才会进行任务切换，实现并发效果
# 协程更适合用在计算类型，比如爬虫

# 同步 异步
# def task():
#     time.sleep(1)
#     print(12345)
#
#
# def sync():
#     for i in range(10):
#         task()
#
#
# def async():
#     g_lst = []
#     for i in range(10):
#         g = gevent.spawn(task)
#         g_lst.append(g)
#     gevent.joinall(g_lst)
#
#
# sync()
# async()


# 协程：能够在一个线程中实现并发效果的概念
#        能规避一些任务中的IO操作
#        在任务的执行过程中，检测到IO就切换到其他任务

# 爬虫的例子
# 请求过程中的IO等待

# 多线程 被弱化
# 协程，在一个线程上，提高CPU的利用率
# 协程比多线程的优势，切换的效率更快



def get_url(url):
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return len(content)


g = gevent.spawn(get_url, 'http://www.google.com')
g1 = gevent.spawn(get_url, 'http://www.sogou.com')
g2 = gevent.spawn(get_url, 'http://www.taobao.com')
g3 = gevent.spawn(get_url, 'http://www.cnblogs.com')
gevent.joinall([g,g1,g2,g3])
print(g.value)
print(g1.value)
print(g2.value)
print(g3.value)

# url = get_url('http://www.google.com')
# print(url)



# socket server