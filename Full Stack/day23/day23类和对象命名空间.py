# 类里，可以定义两种属性
# 静态属性
# 动态属性
# class Course(object):
# 	language = 'Chinese'
# 	def __init__(self):
# 		self.teacher = teacher
# 		self.course_name = course_name
# 		self.period = period
# 		self.price = price

# 不能用__dict__修改
# Course.language = 'English'
# print(Course.language)
# python = Course('egon', 'python', '6 months', 2000)
# Linux = Course('egon', 'Linux', '6 months', 2000)
# print(python.language)
# python.language = 'Chinese'
# del python.language
# print(python.language)
# print(python.__dict__)
# print(Course.language)
# print(Linux.language)
# print(Linux.__dict__)


# 类中的静态变量，可以被对像和类调用
# 对于不可变数据类型来说，类变量最好用类操作
# 对于可变数据类型来说，修改是共享的，重新赋值是独立的

# 模拟人生
# class Person(object):
# 	money = 0
# 	def work(self):
# 		Person.money += 1000

# mother = Person()
# father = Person()
# Person.money += 1000
# Person.money += 1000
# print(Person.money)
# mother.work()
# father.work()


# 创建一个类，没实例化一个对象就记录下来
# 最终所有的对象共享这个数据
# class Foo(object):

# 	count = 0

# 	def __init__(self):
# 		Foo.count += 1

# f1 = Foo()
# f2 = Foo()
# print(f1.count)
# print(f2.count)
# f3 = Foo()
# print(f1.count)



# 认识绑定方法
def func():pass
print(func)

class Foo:
	def func(self):
		print('func')

f1 = Foo()
print(Foo.func)
print(f1.func)
print(f1)


# 包 --- __init__
# import package   # 类的实例化的过程
# import time
# time.time()