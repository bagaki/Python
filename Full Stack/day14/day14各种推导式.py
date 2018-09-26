# [每一个元素或是和元素相关的操作 for 元素 in 可迭代数据类型]  # 遍历之后挨个处理
# [满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]   # 筛选


# 30以内所有嫩被3整出的数
ret = [i for i in range(30) if i % 3 == 0]  # 完整的列表推导式
g = (i for i in range(30) if i % 3 == 0)   # 生成器
print(ret)

# 30以内所有能被3整除的数的平方
ret1 = [i*i for i in range(30) if i % 3 == 0]  # 完整的列表推导式
ret1 = (i*i for i in range(30) if i % 3 == 0)  # 生成器
print(ret1)

# 找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

ret2 = [name for i in names for name in i if name.count('e') == 2]
ret2 = (name for i in names for name in i if name.count('e') == 2)  # 生成器
print(ret2)


#----------------字典推导式----------------------

# 将一个字典的key和value对调
mcase = {'a': 10, 'b': 34}
# mcase = {'10': a, '34': b}
mcase_frequency = {mcase[k]: k for k in mcase}
print(mcase_frequency)


# 合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
print(mcase_frequency)


# ------------------集合推导式--------------------


# 集合推导式，自带结果去重功能
# 计算列表中每个值的平方，自带去重功能
squared = {x**2 for x in [1, -1, 2]}
print(squared)



# 各种推导式： 生成器 列表 字典
#    遍历操作
#    筛选操作