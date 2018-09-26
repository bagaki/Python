# 有多少个模块 - 每个模块大概解决的问题
# 把模块中的所有方法敲一遍

# 代码作业：
# 计算时间差
# 验证码
# 计算器
#!/usr/bin/env python
# coding:utf-8


import re


def deal_minus_issue(calc_list):
    new_calc_list = []
    for index, item in enumerate(calc_list):
        if item.strip().endswith('*') or item.strip().endswith('/'):
            new_calc_list.append('{}-{}'.format(calc_list[index], calc_list[index + 1]))
        elif ('*' or '/') in item:
            new_calc_list.append(item)

    return new_calc_list


def mutilpy_and_dividend(formula):
    print('do it: ', formula)
    calc_list = re.split('[+-]', formula)
    calc_list = deal_minus_issue(calc_list)
    print(calc_list)
    for item in calc_list:
        sub_calc_list = re.split('[*/]', item)
        sub_operator_list = re.findall('[*/]', item)
        print(sub_calc_list, sub_operator_list)
        sub_res = None
        for index, i in enumerate(sub_calc_list):
            if sub_res:
                if sub_operator_list[index-1] == '*':
                    sub_res *= float(i)
                else:
                    sub_res /= float(i)
            else:
                sub_res = float(i)
        return '\33[31;1m[{}]=\33[0m'.format(item, sub_res)

def calc(formula):
    parentheses_flag = True
    while parentheses_flag:
        m = re.search('\([^()]+\)', formula)
        if m:
            print(m.group())
            sub_formula = m.group().strip('()')
            sub_res = mutilpy_and_dividend(sub_formula)
            print('sub_res = ',sub_res)
        continue



if __name__ == '__main__':
    formula = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ) * (-40/5)) - (-4*3)/ (16-3*2) )'
    res = calc(formula)


# 默写
# 验证码