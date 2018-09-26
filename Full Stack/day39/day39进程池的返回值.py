# p = Pool()
# p.map(funcname, iterable)   默认异步的执行任务
# p.apply    同步调用
# p.apply_async  异步调用，和主进程完全异步，要手动close和join
import time
from multiprocessing import Pool


# def func(i):
#     time.sleep(1)
#     return i*i
#
#
# if __name__ == '__main__':
#     p = Pool(4)
#     res_l = []
#     for i in range(10):
#         res = p.apply_async(func, args=(i, ))  # apply的结果就是func的返回值
#         res_l.append(res)
#     for res in res_l: print(res.get())      # 等着func的计算结果，get阻塞等待结果


# ---------map------------
def func(i):
    time.sleep(1)
    return i*i


if __name__ == '__main__':
    p = Pool(4)
    ret = p.map(func, range(10))
    print(ret)