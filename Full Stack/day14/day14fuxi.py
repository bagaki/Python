迭代器和生成器

迭代器：
    双下方法：带双下划线的方法，很少直接调用的，一般情况下是通过其他语法触发的
可迭代的 -- 可迭代协议，含有__iter__的方法 ('__iter__' in dir(数据))
可迭代的一定可以被for循环
迭代器协议：含有__iter__和__next__方法
迭代器一定可迭代，可迭代的通过调用 iter()方法就能得到一个迭代器
迭代器的特点：
    很方便使用，且只能取所有的数据取一次
    节省内存空间


生成器：
生成器的本质就是迭代器
生成器的表现形式：
    生成器函数
    生成器表达式
生成器函数：
    含有yield关键字的函数就是生成器函数
    特点：
        调用函数的时候函数不执行，返回一个生成器
        每次调用next方法的时候会取到一个值
        直到取完最后一个，再执行next会报错

作业：
	有一个文件，从文件里分段读取内容
	readline
	read(10)
	再读出来的内容前面加上一个'***'，再返回给调用者

def generator():
	for i in range(200000):
		yield "product {} wahahha".format(i)

g = generator()  # 调用生成器函数得到一个生成器

print(list(g))  # 数据类的强制转换
# 或者
g.__next__()  # 每一次执行，就是从生成器中取值，预示着生成器函数中的代码继续执行
num = 0
for i in g:
	num += 1
	if num > 50:
		break
	print(i)

# 从生成器中取值的几个方法
    __next__
    for 
    数据类的强制转换：占用内存