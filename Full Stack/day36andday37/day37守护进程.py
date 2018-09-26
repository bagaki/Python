# 守护进程
# 子进程 转换成 守护进程
import time
from multiprocessing import Process


def func():
    while True:
        time.sleep(0.2)
        print('I am live')


def func2():
    print('in func2')
    time.sleep(8)
    print('func2 finished')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True     # 设置子进程为守护进程
    p.start()
    p2 = Process(target=func2)
    p2.start()
    p2.terminate()      # 结束一个子进程
    print(p2.is_alive())  # 检验一个进程是否还活着
    time.sleep(5)
    print(p2.is_alive())
    print(p2.name)
    # i = 0
    # while i < 5:
    #     print('I am socket server')
    #     time.sleep(1)
    #     i += 1

# 守护进程，会随着主进程的代码执行完毕而结束
# 在主进程内结束一个子进程terminate()
#  结束一个进程不是在执行方法之后立即失效，需要一个操作系统响应的过程
# 检验一个进程是否活着的状态