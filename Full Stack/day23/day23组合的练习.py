# 圆形类
# 圆环类

from math import pi


class Circle(object):
	def __init__(self, r):
		self.r = r

	def area(self):
		return self.r ** 2 * pi

	def perimeter(self):
		return 2 * pi * self.r


class Ring(object):

	def __init__(self, outside_r, inside_r):
		self.outside_c = Circle(outside_r)
		self.inside_c = Circle(inside_r)

	def area(self): 
		return self.outside_c.area() - self.inside_c.area()

	def perimeter(self):
		return self.outside_c.perimeter() - self.inside_c.perimeter()

ring = Ring(20, 10)
print(ring.area())
print(ring.perimeter())


# 创建一个老师类  
# 老师有生日
# 生日页可以是一个类
# 组合
class Birthday(object):

	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day


class Course(object):
	language = ['Chinese']
	def __init__(self,teacher,course_name,period,price):
		self.teacher = teacher
		self.course_name = course_name
		self.period = period
		self.price = price


class Teacher(object):

	def __init__(self, name, age, gender, birthday):
		self.name = name
		self.age = age
		self.gender = gender
		self.birthday = birthday
		self.course = Course(self, 'python', '6 month', 20000)

b = Birthday(2018, 1, 16)
egg = Teacher('egon', 30, 'female', b)
print(egg.name)
print(egg.birthday.year)
print(egg.birthday.month)
print(egg.course.price)