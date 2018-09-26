# 面试必考
# 装饰器形成的过程:最简单的装饰器，又返回值的，有一个参数，万能参数
# 装饰器的作用：在不改变元函数的调用方式的情况下，在函数的前后添加功能
# 装饰器的本质：闭包函数
# 语法糖
# 原则（从java中提出）：开放等比原则
# 装饰器的固定模式

# 默写内容：timmer,wrapper

import time


# print(time.time())  # 获取当前时间
# time.sleep(10)  # 让程序在执行到这个位置到的时候停一会
# 语法糖:@装饰器函数名


# 装饰带参数函数的装饰器
# def timmer(f):
# 	def inner(*args, **kwargs):
# 		start = time.time()
# 		ret = f(*args, **kwargs)
# 		end = time.time()
# 		print(end - start)
# 		return ret
# 	return inner

# @timmer
# def func(a, b):
# 	time.sleep(0.01)
# 	print("wahahah", a, b)
# 	return 'muhhahah'
	
# # func = timmer(func)
# rete = func(1, 2)
# print(rete)


# 不想修改函数的调用方式，但是还想再原来的函数前后添加功能
# timmer就是一个装饰器函数，只是对一个函数，有一些装饰作用


# 原则：开放封闭原则
#   开放：对扩展是开放的
#   封闭：对修改时封闭的


# def outer():
# 	def inner():
# 		return 'inner'
# 	inner()



############固定模式###############
def wrapper(f):   # 装饰器函数，f时被装饰额函数
	def inner(*args, **kwargs):
		'''再被装饰函数之前要做的事'''
		ret = f(*args, **kwargs)
		return ret
	return inner

@wrapper
def func(a, b):
	time.sleep(0.01)
	print("wahahah", a, b)
	return 'muhhahah'
	
