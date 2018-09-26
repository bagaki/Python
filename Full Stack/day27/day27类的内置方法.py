# 双下方法
# obj.__str__  str(obj)
# obj.__repr__  repr(obj)
class Teacher:
	def __init__(self,name, salary):
		self.name = name
		self.salary = salary

	def __str__(self):
		return "Teacher's object: %s"%self.name

	def __repr__(self):
		return str(self.__dict__)

	def func(self):
		return 'wahaha'

nezha = Teacher('nezha', 250)
print(nezha)  # a.__str__  --> object
print(repr(nezha))
print('%r'%nezha)
# 打印一个对象的时候，就是调用a.__str__
# object里有一个str，一旦被调用，就返回调用这个方法的对象的内存地址
l = [1,2,3,4]  # 实例化一个列表类的对象
print(l)
print('%s:%s'%('A', a))  # %s  str()  直接打印，实际上都是走的__str__
# %r repr()  实际上都是走的__repr__
# repr是str的备胎
# str不能做repr的备胎
# print(obj)/'%s'%obj/str(obj)的时候，实际上是内部调用了obj.__str__方法，如果str方法有，那么返回的必定是字符串
# 如果没有__str__方法，会先找本类中的__repr__方法，再没有再找父类中的__str__
# repr(),只会找__repr__,如果没有找父类
# def str(obj):
# 	obj.hasattr()
# 
# 内置的方法有很多
# 不一定会都在obj中
class Classes:
	def __init__(self, name):
		self.name = name
		self.student = []

	def __len__(self):
		return len(self.student)

	def __str__(self):
		return 'classes'

py9 = Classes('全站')
py9.student.append('baga')
print(len(py9))
print(py9)


# __del__
class A(object):  # 析构函数:在删除一个对象之前进行一些收尾工作
	# print('执行')
	self.f.close()


a = A()
a.f = open()  # 打开文件，第一，在操作系统中打开了一个文件，拿到了文件操作符存在了内存中
del a        # a.f，拿到了文件操作符消失在内存中
ls = []
for i in range(1000):
	ls.append(A())

a = ls.pop()
# del a   # 即执行这个方法，又删除
# print(a)
import time
time.sleep(3)
print(a)


# __call__
class A(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		'''
		打印这个对象中的所有属性
		'''
		for k in self.__dict__:
			print(k, self.__dict__[k])

a = A('bagaki')()
a = A('baga')
a()