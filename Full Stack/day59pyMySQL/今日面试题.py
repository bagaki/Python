list1 = [11, [22, 3], [4, ], [55, 66], 8, [9, [7, [12, [34, [26]]]]]]
# 取出多余嵌套的列表，得到[11, 22, 3, 4, 55, 66, 8]

# 小剥皮
# [11, [22, 3]]



def f(x):
    ret = []
    for b in x:
        if isinstance(b, list):
            for a in f(b):
                ret.append(a)
        else:
            ret.append(b)
    return ret


list2 = [11, [22, [3,4]]]
ret = f(list1)
print(ret)