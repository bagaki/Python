# 信号量
from multiprocessing import Semaphore
# 原理：用锁的原理实现的，内置了一个计数器
# 在同一时间，只能由指定数量的进程执行某一段被控制住的代码

# 事件
# wait阻塞收到事件状态控制的同步组件
# 状态： True or False 用is_set 来查看
#        True --> False   clear()
#        False --> True   set()
# wait 状态为True不阻塞，False为阻塞

# 何为 锁
#     多个进程在同一时间，只能有一个人进入房间
#     而信号量是，在同一时间，只能有指定的数量进入房间
#     事件是：必须有个信号通过才能执行，修改信号和wait后要做的事，是同步的


# 队列
# Queue
#     put：当队列满了的时候阻塞等待队列有空位置
#     get：当队列空的时候阻塞等待队列有数据
#     full empty，不完全准确
#

# JoinabkeQueue
#     get方法和task_don一起使用
#     put和join


# 今日内容
# 数据gongxManager
# 进程池和回调函数  ******