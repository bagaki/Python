# 面向对象回顾

# 特点
# 1.函数编程：数据和逻辑分离
#     a = 123
#     b = 456
#     c = 789

#     def exc3(proc_name):
#         callproc(xxx)
#         return xxx

#     def exc4(proc_name):
#         callproc(xxx)
#         return xxx

# 2.面向对象：数据和逻辑（属性和行为）组合在一起
# class SqlHelper:
#     def __init__(self):
#         self.host = ''
#         self.port = ''
#         self.db = ''
#         self.charset = ''
#
#     def exc1(self, SQL):
#         # 连接
#         conn(self.host, )
#         execute("insert")
#         return xx
#
#     def exc2(self, proc_name):
#         callproc(xxx)
#         return xxx

#      一类事物共同具有：属性和行为
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

#     1.提取共性
#     2.分裂
#     3.模板“约束”
#     4.当一类韩素供用同样的参数时，可以转变成类进行 - 分类
#     5.面向对象：数据和逻辑（属性和行为）组合在一起
#         函数编程：数据和逻辑分离


# 3.分类示例:
#     类 = 表；对象 = 行
class Userinfo(object):
    def __init__(self, id, name):
        """'约束"每个对象中只有两个字段，即：每个行数据都有id"""
        self.id = id
        self.name = name

    def add(self, name):
        pass

row1 = Userinfo(1, 'alex')
row2 = Userinfo(2, 'alex')

# 特殊方法
class Foo(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    def __call__(self, *args, **kwargs):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

obj1 = Foo('eric')

obj1()
obj1['k']
obj1['k'] = 123
del obj1[k]
obj1.__dict__

# *****************************************************

# 1.ORM 框架：SQLAlchemy
#     作用：
#         1.提供简单的规则
#         2.自动转换成SQL语句

#     DB first:手动创建数据库以及表 -> ORM框架 -> 自动生成类
#     core first：手动创建类、数据库 -> ORM框架 -> 以及表

#     a.功能
#         创建数据库表
#             链接数据库（非SQLAlchemy, 是pymysql）
#             类转换SQL语句
#         操作数据行
#             增删改查
#         便利的工能

# 2.自己开发web框架
#     socket
#     http协议
#     HTML知识
#     数据库（pymysql, SQLALchemy）

