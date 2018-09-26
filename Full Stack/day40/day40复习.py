# 管道：数据不安全，一般用队列
# 数据共享 Manager 数据类型：dict list Queue Pipe，数据仍然不安全
# 进程池
#     为什么要用进程池：节省内存空间，节省创建多个进程带来的时间消耗
#     进程个数：cpu个数+1
#     方法：
#          ret = map(func, iterable)
#              异步，自带close和join
#              所有结果的[]
#          apply
#              同步的
#              ret = apply(func, args=())
#              特点：只有当func执行完之后，才会向下执行其他代码
#              返回值就是func的return
#          apply_async
#               异步的：当func被注册进入一个进程之后，程序就继续向下执行
#               apply_async(func, args=())
#               返回值：apply_async返回的对象
#                   为了用户能从中获取func的返回值obj.get()
#               get会阻塞直到对应的func执行完毕拿到结果
#               使用apply_async给进程池分配任务，需要先close后join来保持多进程和出进程代码的同步性