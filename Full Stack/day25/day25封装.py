# 广义上面向对象的封装：代码的保护，面向对象的思想本身就是一种封装
# 只让自己的对象能调用自己类中的方法

# 狭义上的封装-- 面向对象的三大特性之一
# 属性和方法都藏起来，不让你看见

# 默写
class Person(object):
    __key = 123   # 私有静态属性
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd  = passwd  # 私有属性

    def __get_pwd(self):  # 私有方法
        print(self.__dict__)
        return self.__passwd  # 只要在类的内部使用私有属性，就会自动带上_类名

    def login(self):      # 正常的方法调用私有的方法
        self.__get_pwd()

alex = Person('alex', 'alex3714')
print(alex._Person__passwd)  # _类名__属性名
alex.__high = 1
print(alex.get_pwd())
print(alex.__high)

# 所有的私有，都是在变量的左边加上双下划线
#     对象的私有属性
#     类中的私有方法
#     类中的静态私有属性
# 所有的私有的，都不能在类的外部使用


# 作业：
#