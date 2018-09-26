# class Classes(object):
#     def __int__(self, school, name, kind):
#         self.school = school
#         self.name = name  # 班级名称，例如python_s9
#         self.kind = kind  # 班级科目，例如python go linux
#         self.student = ['student_obj']
#
# class Course(object):
#     def __init__(self, name, period, price):
#         self.name = name
#         self.period = period
#         self.price = price

class Teacher:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.classes = []  # 这个也可以写成组合
        # self.course = Course  # 组合