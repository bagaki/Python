# 多进程代码
from multiprocessing import Process
# 方法
#     进程对象.start()      # 开启一个子进程
#     进程对象.join()       # 感知一个子进程的结束
#     进程对象.terminate()  # 结束一个子进程
#     进程对象.is_alive()   # 查看某个子进程是否还在运行
# 属性
#     进程对象.name         # 进程名
#     进程对象.pid          # 进程号
#     进程对象.daemon       # 值为True的时候，标识新的子进程是一个守护进程
#          守护进程         # 随着主进程代码的执行结束而结束
#                             一定在start之前设置


# Lock：只在多进程里用
from multiprocessing import Lock
# 先实例化
l = Lock()
# 拿钥匙
l.acquire()
# 会造成数据不安全的操作
# 还钥匙
l.release()