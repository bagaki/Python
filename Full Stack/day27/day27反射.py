# 面向对象的进阶
# 其他常用模块
# 作业 考题
# 网络编程 2天
# ftp作业

class A(object):
	pass


class B(A):
	pass

a = A()
print(isinstance(a, A))
print(issubclass(B,A))


# 反射：使用字符串类型的名字，去操作变量
eval('1+2+3')  # 安全隐患


# 反射，就没有安全问题

# 反射对象中的属性和方法
class A(object):
	def func(self):
		print('in func')

a = A()
a.name = 'bagaki'
# 反射对象的属性
ret = getattr(a,'name')  # 通过变量名的字符串形式取到的值
print(ret)

变量名= input('>>>')
print(getattr(a, 变量名))
print(a.__dict__[变量名])

# 反射对象的方法
ret = getattr(a, 'func')
ret()



class A(object):
	price = 20
	@classmethod
	def func(self):
		print('in func')
# 反射类的属性
A.price
print(getattr(A, 'price'))

# 反射类的方法：classmethod  staticmethod
A.func()
if hasattr(A, 'func'):
	getattr(A, 'func')()
ret = getattr(A, 'func')
ret()


# 反射模块的属性
import my
print(my.day)
print(getattr(my, 'day'))

# 反射模块的方法
getattr(my, 'haha')()


# 内置模块也能用
# time
# asctime

def qqxin():
	print('qqxin')
year = 2018
import sys
print(sys.modules['__main__'].year)


# 反射自己模块中的变量和模块
print(getattr(sys.modules['__main__'], 'qqxin'))

# 反射自己模块中的函数
getattr(sys.modules['__main__'], 'qqxin')()

value = input('>>>')
print(getattr(sys.modules[__name__], value))

# 反射的函数有参数怎么办
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(getattr(time, 'strftime')('%Y-%m-%d %H:%M:%S'))
# 一个模块中的类能不能反射得到
# import my
# print(getattr(my, 'C')())
# hasattr(my, 'alex')
# getattr(my, 'alex')
# setattr # 设置修改变量
class A:
	pass
a = A()
setattr(A, 'name', 'alex')
setattr(a, 'name', 'baga')
print(A.name)
print(a.name)

# delattr # 删除一个变量
delattr(a, 'name')
print(a.name)
delattr(A, 'name')
print(a.name)