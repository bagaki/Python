# property
# 内置装饰器函数，只在面向对象中使用
# from math import pi
# class Circle(object):
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def perimeter(self):
#         return 2 * pi * self.r
#
#     @property
#     def area(self):
#         return self.r ** 2 *pi
#
# c1 = Circle(5)
# print(c1.area)
# print(c1.perimeter)

# class Person(object):
#     def __init__(self, name, hight, weight, age, gender):
#         self.name = name
#         self.hight = hight
#         self.weight = weight
#         self.age = age
#         self.gender = gender
#
#     @property
#     def bmi(self):
#         return self.weight / self.hight ** 2
#
#     @property
#     def tzl(self):
#         return 1.2 * self.bmi + 0.23 * self.age - 5.4 -10.8 * self.gender
#
# m = Person('bagaki', 1.54, 60, 26, 0)
# print(m.bmi)
# print(m.tzl)


# class Person(object):
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name + 'sb'
#     @name.setter
#     def name(self, newName):
#         self.__name = newName
#
#
# tiger = Person('taige')
# print(tiger.name)
# tiger.name = 'all'
# print(tiger.name)


# class Goods(object):
#     discount = 0.5
#     def __init__(self,name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.discount
#
# apple = Goods('apple', 5)
# print(apple.price)


# 属性 查看 修改 删除
class Del(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        del self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

d = Del('hener')
print(d.name)
del d.name
print(d.name)

# classmethod
# staticmethod