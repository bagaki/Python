# 回调函数是在主进程中执行的
# 回调函数最多在爬虫上用，在处理数据上用回调函数
from multiprocessing import Pool


def func(n):
    return n + 1


def func1(m):
    print(m)


if __name__ == '__main__':
    p = Pool(5)
    for i in range(10,20):
        p.apply_async(func, args=(i, ),callback=func1)
    p.close()
    p.join()