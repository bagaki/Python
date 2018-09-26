# 多进程中的组件
# 单人ktv

# 一套资源，同一时间，只能被n个人访问
# 某一段代码，同一时间，只能被n个进程执行

import time
import random
from multiprocessing import Process
from multiprocessing import Semaphore


# sem = Semaphore(4)
# sem.acquire()
# print('One')
# sem.acquire()
# print('Two')
# sem.acquire()
# print('fouth')
# sem.acquire()
# print('five')
# sem.acquire()
# print('Three')

def ktv(i, sem):
    sem.acquire()   # 获取钥匙
    print('{} into ktv'.format(i))
    time.sleep(random.randint(1, 5))
    print('{} out ktv'.format(i))
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(20):
        p = Process(target=ktv, args=(i,sem))
        p.start()