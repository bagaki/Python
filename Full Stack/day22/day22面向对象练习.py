# 非常明显的处理一类事物，这些事物都具有相似的属性和功能
# 当有几个函数，需要反反复复传入相同的参数的时候，就可以考虑面向对象
# 这些参数都是对象的属性

# 小明， 10岁， 男， 上山去砍柴
class Person(object):
	"""docstring for Person"""
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def doSomething(self):
		print('{},{}岁，{}，砍柴'.format(self.name, self.age, self.sex))

# circle 属性 半径 两个方法：求周长和面积
# 2pir pir**2
from math import pi
class Circle(object):
	def __init__(self, r):
		self.r = r
	def area(self):
		return pi*(self.r**2)
	def perimeter(self):
		return 2*pi*self.r

c1 = Circle(5)
print(c1.area())
print(c1.perimeter())


# 定义类
# init方法
# self是什么  self拥有属性都属于对象
# 类中可以定义静态属性
# 类中可以定义方法，方法都有一个必须传的参数self
# 实例化
# 示例、对象
# 对象查看属性
# 对象调用方法

# 正方形 周长和面积
class Squir(object):
	def __init__(self, a):
		self.a = a

	def area(self):
		return self.a * self.a

	def perimeter(self):
		return self.a * 4

squir = Squir(9)
area1 = squir.area()
per1 = squir.perimeter()
print(area1, per1)

# 完成人狗大战
# 默写 交互文件