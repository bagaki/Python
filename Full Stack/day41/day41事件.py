# 事件被创建的时候
# False状态
#     wait()  阻塞
# True
#     wait()  非阻塞
# clear 设置状态为False
# set  设置状态为True

# 起两个线程
# 第一个线程：连接数据库
#     等待一个信号，告诉我们之间的网络是痛的
# 第二个线程：检测数据库的可连接情况
#      time.sleep(0,2) 2
#      将事件的状态设置为True
import time
import random
from threading import Thread, Event


def connect_db(e):
    count = 0
    while count < 3:
        e.wait(0.5)   # 状态为False的时候，我只等待1s就结束
        if e.is_set() == True:
            print('连接数据库')
            break
        else:
            print('第{}次连接失败'.format(count))
            count += 1
    else:
        raise  TimeoutError('数据库连接超时')


def check_web(e):
    time.sleep(random.randint(0, 3))
    e.set()

e = Event()
t1 = Thread(target=connect_db, args=(e, ))
t2 = Thread(target=check_web, args=(e, ))
t1.start()
t2.start()



# 数据库
#     文件夹里有好多excel表格
#     alex 81
#          能够更方便的对数据进行增删改查
#          提供了安全访问的机制