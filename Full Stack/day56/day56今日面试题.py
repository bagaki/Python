# 可变对象不能做关键字参数

# def foo(arg, li = []):
#     li.append(arg)
#     return li
#
#
# list1 = foo(21)
# list2 = foo(21, [1,])
# list3 = foo(28)
#
# print(list1)
# print(list2)
# print(list3)

# li.append(arg)是没有返回值的
# def foo(arg, li = []):
#     return li.append(arg)
#
#
#
# list1 = foo(21)
# list2 = foo(21, [1,])
# list3 = foo(28)
#
# print(list1)
# print(list2)
# print(list3)

list4 = [11,22,33,44,55]
# print(list4[10:])

# 打乱列表顺序
import random


random.shuffle(list4)
print(list4)