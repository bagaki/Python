class Classes(object):
    def __init__(self, school, name, course, student_path):
        self.school = school
        self.name = name  # 班级名称，例如python_s9
        self.course = course  # 班级科目，例如python go linux
        self.student_path = student_path

class Course(object):
    def __init__(self, name, period, price, school):
        self.name = name
        self.period = period
        self.price = price
        self.school = school

    def __repr__(self):
        return self.name

class School(object):
    def __init__(self, name, course):
        self.name = name
        self.course = course


# if __name__ == '__main__':
#     from day23.hw_guanli.conf.config import schoolinfo
#     from day23.hw_guanli.core.my_pickle import MyPickle
#     school_pickle = MyPickle(schoolinfo)
#     python = Course('python', '6month', 19800, '北京校区')
#     linux = Course('linux', '5month', 12800, '北京校区')
#     go = Course('go', '4month', 9800, '上海校区')
#     beijing = School('北京校区',[linux, python])
#     shanghai = School('上海校区',[go])
#     school_pickle.dump(beijing)
#     school_pickle.dump(shanghai)
#
#     from day23.hw_guanli.conf.config import course_obj
#     from day23.hw_guanli.core.my_pickle import MyPickle
#     course_pickle = MyPickle(course_obj)
#     python = Course('python', '6month', 19800, '北京校区')
#     linux = Course('linux', '5month', 12800, '北京校区')
#     go = Course('go', '4month', 9800, '上海校区')
#     course_pickle.dump(python)
#     course_pickle.dump(linux)
#     course_pickle.dump(go)