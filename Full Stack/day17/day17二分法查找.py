# 什么叫算法
# 计算的方法：人脑复杂  计算机简单

# 查找： 找数据
# 排序：
# 最短路径

# 我们学习的算法 都是过去时
# 了解基础的算法 才能创造出更好的算法
# 不是所有的事情都能套用现成的方法解决的
# 有些时候会用到学过的算法只是来解决新的问题

# 二分查找算法：必须处理有序d 列表
l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def finds(l, aim):
#     mid = len(l) // 2
#     if l[mid] < aim:
#         new_l = l[mid + 1:]
#         finds(new_l, aim)
#     elif l[mid] > aim:
#         new_l = l[:mid]
#         finds(new_l, aim)
#     else:
#         print("finded it", mid, l[mid])

# def finds(l, aim, start=0, end=len(l)):
#     mid = (end - start) // 2 + start
#     if l[mid] < aim:
#         finds(l, aim, start=mid+1, end=end)
#     elif l[mid] > aim:
#         finds(l, aim, start=start, end=mid-1)
#     else:
#         print('Finded it', mid, aim)


# 找不到
# def finds(l, aim, start=0, end=None):
#     end = len(l) if end is None else end
#     mid = (end - start) // 2 + start
#     if start <= end:
#         if l[mid] < aim:
#             finds(l, aim, start=mid+1, end=end)
#         elif l[mid] > aim:
#             finds(l, aim, start=start, end=mid-1)
#         else:
#             print('Finded it', mid, aim)
#     else:
#         print("We cannot finded it")


# 返回值
def finds(l, aim, start=0, end=None):
    end = len(l) if end is None else end
    mid = (end - start) // 2 + start
    if start <= end:
        if l[mid] < aim:
            return finds(l, aim, start=mid+1, end=end)
        elif l[mid] > aim:
            return finds(l, aim, start=start, end=mid-1)
        else:
            return mid
    else:
        return "We cannot finded it"

ret = finds(l, 44)
print(ret)

# 有问题：
# 参数end
# 返回值
# 找不到的话怎么办


# 三级菜单的代码
# 斐波那契
# 阶乘
# 附加题
# 默写