# 五星重要性
# name = 'alex'


class Teacher(object):
    dic = {'check info':'show_student', 'check teacher':'show_teacher'}
    def show_student(self):
        print('show student')

    def show_teacher(self):
        print('show teacher')

    @classmethod
    def func(cls):
        print('ahha')

alex = Teacher()
for k in Teacher.dic:
    print(k)
key = input('输入需求：')
print(Teacher.dic[key])
fnc = getattr(alex, Teacher.dic[key])
fnc()

# alex = Teacher()
# func = getattr(alex, 'show_student')
# func()

# hasattr  getattr  delattr
# if hasattr(Teacher, 'dic'):
#     ret = getattr(Teacher, 'dic')    # 类也是对象
# # ret1 = getattr(Teacher,'func')   # 类.方法
# # ret1()
#     print(ret)
# menu = Teacher.dic
# for k in menu:
#     print(k)

# 通过反射
# 对象名 获取对象属性和普通方法
# 类名 获取静态属性和类方法和静态方法

# 普通方法self
# 静态方法  @staticmethod
# 类方法    @classmethod
# 属性方法  @property


# 继承
# 封装的


# 管理系统：开发规范
# 整理面向对象的所有知识点
# 时间计划表：周末干什么
#