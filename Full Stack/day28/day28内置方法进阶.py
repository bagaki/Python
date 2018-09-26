# dic = {'k': 'v'}
# # 对象：存储属性和调用方法
# dic['k'] = 'v'
#
#
# class Foo(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __getitem__(self, item):
#         if hasattr(self, item):
#             return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
#
# f = Foo('bagaki', 26, 'female')
# print(f['name'])
# f['hobby'] = 'money'
# print(f.hobby, f['hobby'])
# # del f.hobby    # object原生支持的
# del f['hobby']   # 通过自己实现的
# print(f.__dict__)


# init 初始化方法
# __new__构造方法：创建一个对象
# class A(object):
#     def __init__(self):
#         self.x = 1
#         print('in init function')
#
#     def __new__(cls, *args, **kwargs):
#         print('in new function')
#         return object.__new__(A, *args, **kwargs)
#
# a = A()
# print(a.x)


# 设计模式
# 算法导式
# 23种
# 单利模式
# 一个类始终只有一个实例
# 当你第一次实例化这个类的时候，就创建一个实例化的对象
# 当你之后再来实例化的时候，就用之前创建的对象
# __new__必考（面试）

# class A(object):
#     __instance = False
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance:
#             return cls.__instance
#         cls.__instance = object.__new__(A)
#         return cls.__instance
#
# egon = A('egg', 28)
# egon.cloth = 'xiaohuaao'
# necha = A('enzha', 25)
# print(egon)
# print(necha)
# print(necha.name)
# print(egon.name)
# print(necha.cloth)
#

# class A(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         if self.name == other.name:
#             return True
#         else:
#             return False
#
# obj1 = A('egg')
# obj2 = A('egg')
# print(obj1 == obj2)


# hash()   # __hash__
# class A(object):
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def __hash__(self):
#         return hash(self.name + self.sex)
#
# a = A('egon', 'male')
# b = A('egon', 'female')
# print(hash(a))
# print(hash(b))
# import json
# from collections import namedtuple
# Card = namedtuple('Card', ['rank', 'suit'])
# # c1 = Card(2, '梅花')
# # print(c1)
# # print(c1.suit)
#
# class FranchDeck(object):
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = ['红心','方块','梅花','黑桃']
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for rank in FranchDeck.ranks
#                        for suit in FranchDeck.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#
#     def __str__(self):
#         return json.dumps(self._cards, ensure_ascii=False)
#
# deck = FranchDeck()
# print(deck[0])
# from random import choice
# print(choice(deck))
# print(choice(deck))
# from random import shuffle
# shuffle(deck)
# print(shuffle(deck))
# print(deck)
# print(deck[:5])

# 内置函数 内置的模块 内置的基础类型 < --- >类的内置方法
# ==  __eq__
# len()  __len__


# class A(object):
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def __eq__(self, other):
#         if self.name == other.name and self.sex == other.sex:
#             return True
#         return False
#
#     def __hash__(self):
#         return hash(self.name + self.sex)
#
# a = A('egg', 'mela', 38)
# b = A('egg', 'mela', 37)
# print(set((a, b)))

# set依赖对象的 hash和eq方法