# class Classes(object):
#     def __int__(self, school, name, course, student_path):
#         self.school = school
#         self.name = name  # 班级名称，例如python_s9
#         self.course = course  # 班级科目，例如python go linux
#         self.student_path = student_path
#
# class Course(object):
#     def __init__(self, name, period, price):
#         self.name = name
#         self.period = period
#         self.price = price

class Student:
    def __init__(self, name, school, clas):
        self.name = name
        self.school = school
        self.clas = clas
        # self.course = Course  # 组合