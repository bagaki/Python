"""
执行完下面的代码后，l，m的内容分别是什么
"""
from copy import deepcopy


def func(m):   # l = {1:2, 3:4, 9:10}
    for k, v in m.items():
        m[k+2] = v+2   # m[3] = 4   m[5] = 6


m = {1:2, 3:4}
l = m
l2 = deepcopy(m)
l[9] = 10  # l = {1:2, 3:4, 9:10}
l2[90] = 100
# func(l)
m[7] = 8

print(l)
print(m)
print(l2)

# 遍历一个字典的时候，能不能对字典本身做涉及键的操作
# 深浅拷贝的理解

