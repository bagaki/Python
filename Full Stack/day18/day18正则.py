# 计算器
# re模块
# 正则表达式 -- 字符串匹配的
# 学习正则表达式
# 学习使用re模块来操作正则表达式


import re


# 大作业
a = 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# 去掉所有空格
# 加减乘除 括号
# 先算括号里的乘除，再算括号里的加减、
# 从括号里取值 == 正则表达式
# ss = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 '
# 从一个没有括号的表达式中取 */法 == 正则表达式


# 复习
# 元字符  量词
# re模块


# 练习题


# 大作业
# 计算器

# 从括号里取值 == 正则表达式

def calc(formule):
    '''
    将公式从字符串中提取出来，找到最里层的括号
    :param formule: 公式
    :return:
    '''
    pass


def mul_devi(formule):
    '''
    处理最里层括号中的乘除，以+和-分割，将乘除公式分割出来，将新列表返回给minus_issue
    :param formule:
    :return:
    '''
    pass

def minus_issue(new_calc):
    '''
    接收到mul_devi的新列表，开始处理列表中需要乘除运算的元素，将需要处理的元素组成新的列表，返回给mul_devi
    :param new_calc: mul_devi传过来的列表
    :return: 新列表，剩下乘除运算的元素
    '''
    pass


if __name__ == '__main__':
    ret = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    calc(ret)