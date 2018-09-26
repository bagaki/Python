# 1、默写三层装饰器，标注代码的执行步骤
#
# 2、整理作业：函数的知识点以及装饰器相关作业。装饰器作业需要自己写一遍，并给作业加注释
#
# 3、周末大作业：实现员工信息表
# 文件存储格式如下：
# id, name, age, phone, job
# 1, Alex, 22, 1365104808, IT
# 2, Rgon, 34, 13304320533, Teacher
# 3, nzha, 25, 133235322, IT
#
# 现在需要对这个员工信息文件进行增删改查
# 基础必做：
# a、可以进行查询，支持三种语法：
#     select 列名1, 列名2, where 列名条件
#     支持：大于小于等于，还要支持模拟查找
# 示例：
#     select name, age where age>22
#     select * where job=IT
#     select * where phone like 133
#
#
# 进阶选做：
# b、可创建新员工记录，直接输入员工id即可
# c、可删除指定员工记录，直接输入员工id即可
# d、修改员工信息
# 语法：set 列名 = '新的值' where 条件
#  先用where查找对应人的信息，再使用set来修改列名对应的值为'新的值'
#
# 注意：要想操作员工信息表，必须先登录，登录认证需要用装饰器完成
# 其他需求尽量使用函数实现

# 例子

# 思维导图
# 员工信息表：完善代码

# 读取文件 -- 将文件中的内容整理到
dic = {'id': 0, 'name': 1, 'age': 2, 'phone': 3, 'job': 4}


def get_line(filename):
    with open(filename, encoding='utf-8') as f:
        for i in f:
            i = i.strip()
            lst = i.split(',')
            yield lst


def condition_filter(condition):
    '''条件筛选'''
    condition = condition.strip()
    if '>' in condition:
        col, val = condition.split('>')
        g = get_line('staff_info.txt')
        for line_lst in g:
            if int(line_lst[dic[col]]) > int(val):
                yield line_lst
    elif '<' in condition:
        col, val = condition.split('<')
        g = get_line('staff_info.txt')
        for line_lst in g:
            if int(line_lst[dic[col]]) < int(val):
                yield line_lst

    elif '=' in condition:
        col, val = condition.split('=')
        g = get_line('staff_info.txt')
        for line_lst in g:
            if int(line_lst[dic[col]]) == int(val):
                yield line_lst

    elif 'like' in condition:
        col, val = condition.split('like')
        g = get_line('staff_info.txt')
        for line_lst in g:
            if int(line_lst[dic[col]]) == int(val):
                yield line_lst


def views(view_lst, staff_g):  # view_lst = ['name', 'age]
    '''
	展示符合条件的员工信息
	:return:
	'''
    if '*' in view_lst:
        view_lst = dic.keys()
    for staff_info in staff_g:
        for i in view_lst:
            print(staff_info[dic[i]], end=' ')
        print('')

# 接收用户的信息 -- 分析信息
# ret = input('>>>')
ret = 'select * where phone like 137'
view, condition = ret.split('where')
view = view.replace('select', '').strip()
view_list = view.split(',')
print(view_list, condition)
g = condition_filter(condition)
views(view_list, g)