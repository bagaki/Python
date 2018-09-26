# 双下方法：用C语言写好的方法，不止一种方法可以调用它

# 迭代器
l = [1, 2, 3]
# 索引
# 循环 for
#     for i in l:

# 可以被for循环:
# list
# dic
# str
# tuple
# f = open 
# range()
# enumerate
print(dir([]))  # 告诉我列表拥有的所有方法
print(dir({}))  # 告诉我列表拥有的所有方法
print(dir(''))  # 告诉我列表拥有的所有方法
print(dir(range(10)))  # 告诉我列表拥有的所有方法
ret = set(dir([]))&set(dir({}))&set(dir(''))&set(dir(range(10)))
print(ret)  # iterable
print('__iter__' in dir(int))
print('__iter__' in dir(list))
print('__iter__' in dir(dict))
print('__iter__' in dir(set))
print('__iter__' in dir(tuple))
print('__iter__' in dir(enumerate([])))
print('__iter__' in dir(range(10)))

# 只要时能被for循环的数据类型，就一定拥有__iter__方法
print([].__iter__())
# 一个列表执行了__iter__()之后的返回值就是一个迭代器

iterator = l.__iter__()
print(iterator.__next__())

# Iterable 可迭代的 -- 》  __iter__  # 只要含有__iter__方法的都可迭代的
# [].__iter__() 迭代器 -- 》 __next__  # 通过__next__就可以从迭代器中一个一个的取值

# 只要含有__iter__方法的都可迭代的 --- 可迭代协议
# 迭代器协议 --- 内部含有__next__和__iter__方法的就是迭代器
print('__iter__' in dir([].__iter__()))
print('__next__' in dir([].__iter__()))

from collections import Iterable, Iterator
print(isinstance([], Iterator))
print(isinstance([], Iterable))

class A:
	def __iter__(self):pass
	def __next__(self):pass

a = A()
print(isinstance(a, Iterator))
print(isinstance(a, Iterator))


# 迭代器的概念
# 迭代器协议 --- 内部含有__next__和__iter__方法的就是迭代器

# 迭代器协议和可迭代协议
# 可以被for循环的都是可迭代的
# 可迭代的内部都有__iter__方法
# 只要是迭代器一定可以迭代
# 可迭代的__iter__()方法就可以得到一个迭代器
# 迭代器中的__next__()方法可以一个一个的获取值

# for循环就是在使用迭代器
# iterator
# 可迭代对象
# 直接给你内存地址
print([].__iter__())
print(range(10))


# 迭代器的好处：
#    从容器类型中一个一个的取值，会把所有的值都取到
#    节省内存空间
#        迭代器并不会在内存中再占用一大块内存，
#            而是随着循环，每次生成一个，每次next每次给我一个

# range
# f = open()
l = [1,2,3,4,5]
iter = l.__iter__()
while True:
	print(iterator.__next__())



# 生成器  --  迭代器
# 生成器函数 -- 本质上就是我们自己写的函数
# 生成器表达式

l = [1,2,3,4,5]
for i in l:
	print(i)
	if i == 2:
		break

for i in l:
	print(i)