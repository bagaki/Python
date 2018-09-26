# login 登录
# log 日志
# logging

# 什么叫日志？
# 日志是用来记录用户行为 或者 代码的执行过程
# print

# logging
# 能够“一键”控制
# 排错的时候需要打印很多细节来帮助我排错
# 严重的错误记录下来
# 有一些用户行为：有没有错都要记录
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a'
#
# try:
#     int(input('num >> '))
# except ValueError:
#     logging.error('The input is not number')


# logging.debug('debug message')         # 低级别的
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')  # 高级别

# basicconfig 简单 能做的事情相对少
#     中文的乱码问题
#     不能同时往文件和屏幕上输出
# 配置log对象 稍微优点复杂，能做的事情相对多

import logging

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log',encoding='utf-8')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setLevel(logging.DEBUG)

# 文件操作符 和 格式关联
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# logger对象 和 文件操作符 关联
logger.addHandler(fh)   # logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logging.debug('debug message')         # 低级别的
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')  # 高级别

# 程序的充分解耦
# 让程序变得高可定制

# zabbix 监控系统


# 有5种级别的日志记录模式：
# 两种配置方式：basicconfig、log对象

# django框架