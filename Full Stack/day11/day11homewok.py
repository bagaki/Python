# 1、编写装饰器，为多个函数加上认证的功能
# 要求登录成功依次，后续的函数都无需再输入用户名和密码
FALG = False
def login(func):
	def inner(*args, **kwargs):
		global FALG
		'''登录程序'''
		if FALG:
			ret = func(*args, **kwargs)
			return ret
		else:
			username = input("please input your name:")
			pwd = input("please input your password:")

			if username == 'bagaki' and pwd == '123456':
				FALG = True
				ret = func(*args, **kwargs)
				return ret
			else:
				print("Login is false")
	return inner

@login
def shoplist_add():
	print('Add something')

@login
def shoplist_del():
	print('Delete something')

shoplist_add()
shoplist_del()


# 2、编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
def log(func):
	def inner(*args, **kwargs):
		with open('log', 'a', encoding='utf-8') as f:
			f.write(func.__name__ + '\n')
		ret = func(*args, **kwargs)
		return ret
	return inner


@log
def shoplist_add():
	print('Add something')

@log
def shoplist_del():
	print('Delete something')

shoplist_add()
shoplist_del()


# 进阶作业“
# 1、编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
from urllib.request import urlopen

def get(url):
	hl = urlopen(url).read
	return code

ret = get('http://baidu.com')
print(ret)

# 2、为题目1编写装饰器，实现缓存网页内容的功能
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后
import os
from urllib.request import urlopen

def cache(func):
	def inner(*args, **kwargs):
		if os.path.getsize('web_cache'):
			with open('web_cache', 'rb') as f:
				return f.read()

		ret = func(*args, **kwargs)
		with open('web_cache', 'wb') as f:
			f.write(b'*********' + ret)
		return ret
	return inner

@cache
def get(url):
	hl = urlopen(url).read
	return code

# {'网址': '文件名'}
ret = get('http://baidu.com')
print(ret)

ret = get('http://www.baidu.com')
print(ret)

ret = get('http://www.baidu.com')
print(ret)