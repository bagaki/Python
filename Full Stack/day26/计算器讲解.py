import re

# 表达式
def dealwith(express):
    # 将表达式中的符号处理+-替换成-， --替换成+
    express = express.replace('+-', '-')
    express = express.replace('--', '+')
    return express


def cal_exp_son(exp_son):
    # 只用来计算原子型的表达式，两个数之间的乘除法
    if '/' in exp_son:
        a,b = exp_son.split('/')
        return str(float(a)/float(b))
    elif '*' in exp_son:
        a,b = exp_son.split('*')
        return str(float(a)*float(b))



def cal_express_no_bracket(exp):
    # 计算没有括号的表达式
    # exp是没有经过处理的最内层带括号的表达式
    exp = exp.strip('()')
    # print(exp)
    # 先乘除后加减
    while True:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', exp)  # 匹配第一个乘除
        if ret:  # 说明表达式中嗨哟乘除法
            exp_son = ret.group()   # 子表达式，最简单的乘除法
            print(exp_son)
            ret = cal_exp_son(exp_son)
            exp = exp.replace(exp_son, ret)
            exp = dealwith(exp)
        else: # 说明表达式中没有乘除了
            ret = re.findall('-?\d+\.?\d*', exp)
            sum = 0
            for i in ret:
                sum += float(i)
            return str(sum)
    
    


# 提取括号里面没有其他括号的表达式
def remove_bracket(newExpress):
    while True:
        ret = re.search('\([^()]+\)', newExpress)
        if ret:
            express_no_bracket = ret.group()   # 表达式，没括号
            print('匹配不到括号', express_no_bracket)
            ret = cal_express_no_bracket(express_no_bracket)
            newExpress = newExpress.replace(express_no_bracket, ret)
            print('***'+newExpress)
            newExpress = dealwith(newExpress)
        else:
            print('no more bracket',newExpress)
            ret = cal_express_no_bracket(newExpress)
            return ret



express = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ) * (-40/5)) - (-4*3)/ (16-3*2) )'
# 去空格
newExpress = express.replace(' ', '')
print(newExpress)
ret = remove_bracket(newExpress)
print(ret)

s = eval(express)
print(s)