"""
有一个列表[11, 2, 3, 3, 7, 9, 11, 2], 去重并且保持原来的顺序
"""
l = [11, 2, 3, 3, 7, 9, 11, 2]
l1 = list(set(l))
l1.sort(key=l.index)
print(l1)