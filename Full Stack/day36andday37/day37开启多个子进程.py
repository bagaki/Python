import os
import time
from multiprocessing import Process


# def func(arg1, args2):
#     print('*'*arg1)
#     time.sleep(2)
#     print('='*args2)
#
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(10):
#         p = Process(target=func, args=(10*i, 20*i))
#         p_lst.append(p)
#         p.start()
#     [p.join() for p in p_lst]
#     print('运行完了')


def func(filename, content):
    with open(filename, 'w') as f:
        f.write(content*10*'*')


if __name__ == '__main__':
    p_lst = []
    for i in range(5):
        p = Process(target=func, args=('info{}'.format(i), i))
        p_lst.append(p)
        p.start()
    [p.join() for p in p_lst]   # 之前的所有进程必须在这里都执行完才能执行下面的代码
    print([i for i in os.walk(r'D:\program\oldmantest\quanzhan\day36andday37')])

# 同步： 0.1 * 500 = 50
# 异步： 500 0.1   = 0.1
# 多进程写文件
# 首先往文件中写文件
# 像用户展示写入文件之后文件夹中所有的文件名