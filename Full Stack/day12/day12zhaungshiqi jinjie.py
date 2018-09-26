# 装饰器的进阶
#     functools wraps
#     带参数的装饰器
#     多个装饰器装饰同一个函数


# functools wraps
from functools import wraps

 def wrapper(f):
 	@wraps(f)
	def inner(*args, **kwargs):
		print('在被装饰的函数执行之前做得事')
		ret = f(*args, **kwargs)
		print('在被装饰的函数执行之后做得事')
		return ret
	return inner

@wrapper
def holiday(day):    # holiday = wrapper(holiday)
	print('放假{}天'.format(day))
	return 'ureshi'

print(holiday.__name__)
# ret = holiday(3)   # inner
# print(ret)


def wahah():
	'''
	一个打印wahaha的函数
	'''
	print('wahha')

print(wahah.__name__)
print(wahah.__doc__)


# 带参数的装饰器
# 500个函数
import time

FLAGE = True

def timmer_out(flage):
	def timmer(func):
		def inner(*args, **kwargs):
			if flage:
				start = time.time()
				ret = func(*args, **kwargs)
				end = time.time()
				print(end - start)
				return ret
			else:
				ret = func(*args, **kwargs)
				return ret
		return inner
	return timmer

# timmer = timmer_out(FLAGE)

@timmer_out(FLAGE)
def wahaha():
	time.sleep(0.1)
	print("hahahaha")

@timmer_out(FLAGE)
def erguotou():
	time.sleep(0.1)
	print("toutoutou")

wahaha()
erguotou()



# 多个装饰器装饰同一个函数
def wrapper1(func):  # func ---> f
	def inner1():
		print('wrapper1 before func')
		ret = func()  # f
		print('wrapper1 after func')
		return ret
	return inner1

def wrapper2(func):  # func --> inner1
	def inner2():
		print('wrapper2 before func')
		ret = func()  # inner1
		print('wrapper2 after func')
		return ret
	return inner2

def wrapper3(func):  
	def inner3():
		print('wrapper3 before func')
		ret = func()  
		print('wrapper3 after func')
		return ret
	return inner3

@wrapper3
@wrapper2  # f = wrapper2(f) --> wrapper2(inner1)
@wrapper1  # f = wrapper1(f) == inner1
def f():
	print('in f')
	return 'kakaka'

print(f()) # -->inner2()


# 记录用户的登录情况
# 计算这个函数的执行时间




# Python核心编程