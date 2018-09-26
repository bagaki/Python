# 超过最大递归限制的报错
# 只要写递归函数，必须要有结束条件

# 返回值
# 不要只看到return就认为已经返回了，要看返回操作是在递归到第几层的时候发生的，然后返回给了谁
# 如果不是返回给最外层函数，调用者就接收不到
# 需要再分析，看如何把结果返回回来

# 循环 --
# 递归

# 斐波那契
# 1，1，2，3，5，8
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)  # fib(3) + fib(2) = fib(2) + fib(1) + 1
print(fib(4))
# 最好不要用双递归
# 单递归
# def fib(n):
#     a, b = fib(n-1)

# fib(3)

# 阶乘
def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)
print(fac(5))

# 附加题


# 默写