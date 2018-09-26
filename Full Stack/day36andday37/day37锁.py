# 锁

# 默写
# 火车票
import json
import time
from multiprocessing import Process
from multiprocessing import Lock


def show(i):
    with open('ticket') as f:
        dic = json.load(f)
    print('余票:{}'.format(dic['ticket']))


def buy_ticket(name, lock):
    lock.acquire()  # 拿钥匙进门
    with open('ticket') as f:
        dic = json.load(f)
        time.sleep(0.1)
    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        print('{} buy it'.format(name))
    else:
        print('{} got Nothing'.format(name))
    time.sleep(0.1)
    with open('ticket', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=show, args=(i,))
        p.start()
    lock = Lock()
    for i in range(10):
        p = Process(target=buy_ticket, args=(i, lock))
        p.start()