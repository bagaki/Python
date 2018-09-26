'''
需求：
角色:
学校、学员、课程、讲师

要求:
1. 创建北京、上海 2 所学校

2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开

3. 课程包含，周期，价格

4. 班级关联课程、讲师

5. 创建学员时，选择学校，关联班级

5. 创建讲师角色时要关联学校

6. 提供三个角色视图

　　6.1 学员视图， 登陆， 查看课程、查看班级

　　6.2 讲师视图， 讲师可查看自己教学的班级、课程。

　　　　　　　　　 进阶需求：可管理自己的班级， 查看班级学员列表 ， 修改所管理的学员的成绩

　　6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里
'''


class Course(object):

    def __init__(self, teacher, course_name, period, price):
        self.teacher = teacher
        self.course_name = course_name
        self.period = period
        self.price = price


class Scoohle(object):

    def __init__(self, bj, sh, Course):
        self.bj = bj
        self.sh = sh
        # self.course = Course

    # self.course = self.Course()

    def bj(self, linux, python):
        self.Course = Course
        self.Course('bagaki', 'python', 6, 20000)

    def sh(self, go):
        self.Course('bagaki', 'go', 6, 20000)


class Log(object):

    def __init__(self, students, teachers, admin):
        self.students = students
        self.teachers = teachers
        self.admin = admin

    def students(self):
        '''
        学生视图：登录，查看课程，查看班级
        '''
        pass

    def teacher(self):
        '''
        讲师视图：查看自己班级、课程
                    进阶需求：可管理自己的班级、查看学生列表、此u该所管理的学生的成绩
        '''
        pass

    def admin(self):
        '''
        管理视图：创建讲师、创建班级、创建课程
        '''
        pass
