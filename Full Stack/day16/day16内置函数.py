# 主要内容在day15内置函数.py，这边做扩展

# 原由的列表就找不到了
reversed()
l = [1,2,3,4,5]
l.reverse()
print(l)

# 保留原来列表，返回一个反向迭代器
l1 = reversed(l)
print(l1)

l = (1,2,23,213,5612,342,43)
sli = slice(1,5,2)
print(l[sli])
print(l[1:5:2])


print(format('test','<20'))   # 左对齐
print(format('test','>20'))   # 右对齐
print(format('test','^20'))   # 居中

# bytes 转换成bytes类型
# 拿到的是gbk时，已经时bytes类型了，但我想转成utf-8
print(bytes('你好',encoding='GBK').decode('GBK'))
print(bytes('你好',encoding='utf-8'))   # unicode转换成utf-8的bytes


# 网络编程 只能传二进制
# 照片和视频也是以二进制存储
# html网页爬去到的也是编码

b_array = bytearray('你好',encoding='utf-8')
print(b_array)
print(b_array[0])


l = 'sdhdkashhahaha'
# 切片 字节类型 不沾内存
# memoryview


name = 'egg'
print('Hello %r'%name)
print(repr('1'))
print(repr(1))


print(all(['a', '', 123]))  # False
print(all(['a', 123]))      # True
print(all([0, 123]))        # False

print(any(['', True, 0, []]))  # True


# zip
l = [1,2,3]
l1 = ['a', 'b', 'c']
l2 = ('*', '***', [12,2])
d = {'k1':1, 'k2':2}
for i in zip(l, l1, l2):
	print(i)


# filter
def is_odd(x):
	return x % 2 == 1

# 过滤数字，只要字符串
def is_str(s):
	return type(s) == str

# 去掉空内容
def is_kara(s):
	return s and str(s).strip()

ret = filter(is_odd, [1,4,None,6,7,9,12,17])
ret = filter(is_str, [1, '','',4,None,6,'hello',7,9,'world',[],12,17])


from math import sqrt

# 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def func(num):
	ret = sqrt(num)
	return ret % 1 == 0

ret = filter(func, range(1,101))
for i in ret:
	print(i)


# map
ret = map(abs, [1,-4,6,-8])
print(ret)
for i in ret:
	print(i)


# filter 执行了filter之后的结果集合 <= 执行之前的个数
#        filter中只管筛选，不会改变原来的值
# map：执行前后个数不变
#      值可以发生改变

# sort
l = [1,-4,6,5,-10]
l.sort(key = abs)  # 在原列表的基础上进行排序
print(l)

# sorted：返回整个列表，不改变原列表，占内存
print(sorted(l))

# 列表按照其中每一个值的绝对值排序
l = ['   ', [1,2], 'hello world']
new_l = sorted(l, key=len)
print(new_l)

add = lambda x,y :x + y
dic = {'k1':19, 'k2':100, 'k3':30}
print(max(dic, key=lambda k:dic[k]))

def func(x):
	return x>0

res = filter(lambda x:x>10, [5,8,11,9,15])
for i in res:
	print(i)

# 带key的很重要
# min max filter map sorted -- 可以和lambda合作


# 面试题
d = lambda p:p*2
t = lambda p:p*3
x =2 
x = d(x)  # 4
x = t(x)  # 12
x = d(x)  # 24
print(x)

# 2.现有两元组(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# max min sorted filter map
# 匿名函数 == 内置函数
# zip
# ret = zip((('a'),('b')),(('c'),('d')))
# def func(tup):
# 	return {tup[0]:tup[1]}
# res = map(lambda tup:{tup[0]:tup[1]}, zip((('a'),('b')),(('c'),('d'))))
print(list(map(lambda tup:{tup[0]:tup[1]}, zip((('a'),('b')),(('c'),('d'))))))

# 3.以下代码的输出是什么？请给出答案并解释。
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# 以上结果时[6,6,6,6]
# 请修改multipliers的定义来产生期望的结果。
def multipliers():
    return (lambda x:i*x for i in range(4))
print([m(2) for m in multipliers()])