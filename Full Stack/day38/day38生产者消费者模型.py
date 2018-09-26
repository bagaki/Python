# 队列
# 生产者消费者

# 生产者 进程
# 消费者 进程
import time
import random
from multiprocessing import Process, JoinableQueue


def consumer(q, name):
    while True:
        food = q.get()
        if food is None:
            print('{}获取到一个空'.format(name))
            break
        print('\033[31m{} buy {}s\033[0m'.format(name, food))
        time.sleep(random.randint(1, 3))
        q.task_done()


def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        f = '\033[32m{} produce {} {}\033[0m'.format(name, i, food)
        print(f)
        q.put(f)
    q.join()  # 阻塞，直到一个队列中的数据，全部被执行完毕

if __name__ == '__main__':
    q = JoinableQueue(20)
    p = Process(target=producer, args=('bagaki', 'bread', q))
    p.start()
    p1 = Process(target=producer, args=('tomoya', 'sweet', q))
    p1.start()
    c = Process(target=consumer, args=(q, 'shikeko'))
    c.daemon = True   # 设置为守护进程，主进程中的代码执行完毕之后，子进程，也就是该守护进程自动结束
    c.start()
    c1= Process(target=consumer, args=(q, 'ani'))
    c1.daemon = True
    c1.start()

    p.join()   # 感知一个进程的结束
    p1.join()


# 在消费者这一端：
#     每次获取一个数据
#     处理一个数据
#     发送一个记号：标志一个数据被处理成功

# 在生产者这一端：
#      每一次生产一个数据
#      且每一从生产的数据都放在队列中
#      在队列中刻上一个记号
#      当生产者全部生产完毕之后
#      发送join信号：已经停止生产数据了
#          且要等待之前被刻上的记号都被消费完
#          当数据都被处理完时，join阻塞结束

# consumer开始，吧所有的任务消耗完
# producer端的join感知到，停止阻塞
# 所有的producer进程结束
# 主进程中的p.join结束
# 主进程中的代码结束
# 守护进程（消费者进程）结束