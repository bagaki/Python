import os 
import time
import day12homewok_sample


def search_parse():
	print('''\t\t\t-----------------------------------
				select name, age where age>22
				select * where job=IT
				select * where phone like 133
\t\t\t-----------------------------------''')

FLAGE = True

def check(flage):
	def login(func):
		def inner(*args, **kwargs):
			'''登录程序'''
			if flage:
				username = input("please input your name:")
				pwd = input("please input your password:")

				if username == 'bagaki' and pwd == '123456':
					flage
					ret = func(*args, **kwargs)
					return ret
				else:
					print("Login is false")
			else:
				ret = func(*args, **kwargs)
				return ret
		return inner
	return login


@login
def search():
	pass

def add():
	pass

def dele():
	pass

def upd():
	pass