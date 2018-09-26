import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(2)
    print(n)
    return n*n


def call_back(m):
    print('结果是{}'.format(m.result()))


# 进程池，改这里就好了
tpool = ThreadPoolExecutor(max_workers=5)  # 默认不要cpu个数*5
# tpool.map(func, range(20))  # map拿不到返回值
# t_lst = []
# for i in range(20):
#     t = tpool.submit(func, i)
#     t_lst.append(t)
# # tpool.shutdown()  # close + join
# print('主线程')
# for t in t_lst:
#     print('***', t.result())
# 回调
for i in range(20):
    tpool.submit(func, i).add_done_callback(call_back)

# 并发编程必须整理