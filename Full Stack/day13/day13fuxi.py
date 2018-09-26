# 函数
#    函数的定义和调用
#    def 函数名(形参):
#        函数体
#        return 返回值
#    调用 函数名(实参)
#    站在形参的角度上：位置参数，*args，默认参数(陷阱)，**kwargs
#    站在实参的角度上：按照位置传，按照关键字传
#    返回值：没有返回值，返回一个值，返回多个值
#    接收返回值：没有返回值不接受，返回一个值用一个变量接收，返回多个值用一个变量或对应数目的变量接收
# 


# 闭包函数 --- 再内部函数引用外部函数的变量
# 装饰器函数 --- 装饰器一定是闭包函数
#    装饰器的作用：在不改变原来函数的调用方式的情况下，在这个函数的前后添加新的功能
#    完美的符合了一个开发原则；开放封闭原则
#        对扩展是开放的
#        对修改时封闭的
#    基础的装饰器
# 	 完美的装饰器
#    from functools import wraps
#    def wrapper(f):
#        @wraps(func)
#        def inner(*args, **keargs):
#            ''''在函数被调用之前添加的代码'''
#            ret = f(*args, **kwargs)
#            ''''在函数被调用之后添加的代码'''
#            return ret
#        return inner
#    带参数的装饰器
#    @wrapper --> @wrapper(argument)
#    三层嵌套函数
#    def outer(形参):
#        def wrapper(f):
#            def inner(*args, **keargs):
#                ''''在函数被调用之前添加的代码'''
#                ret = f(*args, **kwargs)
#                ''''在函数被调用之后添加的代码'''
#                return ret
#            return inner
#         return wrapper
#     @outer(True)
#     def func():
#         pass
#
#     多个装饰器装饰一个函数
#          俄罗斯套娃
#          @wrapper1
#          @wrapper2
#          @wrapper3