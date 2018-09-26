'''
默写：
L = [1,2,3,4]
def pow2(s):
    return s*s

print(list(map(pow2, L)))
结果：
[1,4,9,16]



def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd, [1,4,6,7,9,12,17])))
结果：
[1,7,9,17]
'''

# 3、用map来处理字符串列表，把列表中所有人都编程sb，比如alex_sb
name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']


def sb(i):
    return i + ' sb'

print(list(map(sb, name)))

# 4、有filter函数处理数字列表，将列表中所有的偶数筛选出来
num = [1,3,5,6,7,8]


def is_not_odd(x):
    return x % 2 == 0


print(list(filter(is_not_odd, num)))


# 5、随意写一个20行以上的文件
# 运行程序，先将内容读到内存中，用列表存储
# 接收用户输入页码，每页5条，仅输出当页的内容
# with open('suiyi.txt', encoding='utf-8') as f:
#     l = f.readlines()
#
# page_num = int(input('Please input the number:'))
# pages,mod = divmod(len(l), 5)  # 求有多少页，有没有剩余的行数
# if mod:         # 如果有剩余的行数，那么页数加一
#     pages += 1   # 一共有多少页
# if page_num > pages or page_num <= 0:    # 用户输入的页数大于总数或小于等于0
#     print('The input is wrong')
# elif page_num == pages and mod != 0:    # 如果用户输入的页码是最后一页，且之前有过剩余行数
#     for i in range(mod):
#         print(l[(page_num-1)*5 + i].strip())    # 值输出这一夜上剩余的行
# else:
#     for i in range(5):
#         print(l[(page_num-1)*5 + i].strip())  # 输出5行


# 6、如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]

# 计算购买每支股票的总价
ret = map(lambda  dic: {dic['name']:round(dic['shares'] * dic['price'], 2)}, portfolio)
print(list(ret))
# 用filter过滤出，单价大于100的股票有哪些
def func(dic):
    if dic['price'] > 100:
        return (dic)

print(list(filter(func, portfolio)))