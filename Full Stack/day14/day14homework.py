# 默写
# 生成器函数（含预激活）
def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g

    return inner


@init
def average():
    sm = 0
    counts = 0
    avg = 0
    while True:
        num = yield avg
        sm += num
        counts += 1
        avg = sm / counts


avg_g = average()
ret = avg_g.send(10)
print(ret)


# 生成器表达式
s = ('suibia{}'.format(i for i in range(10)))
print(s)
print(next(s))
print(next(s))



# 1、通过迭代器生成器博客，将所有示例敲一遍，务必弄明白
# 2、知识点结构图

# 3、处理文件，用户指定要查找的文件和内容  (open)
#    将文件中含要查的每一行都输出到屏幕  生成器循环输出
def check_file(filename, aim):
    with open(filename, encoding='utf-8') as f:  # 句柄：handler，或文件操作符，文件对象
        for i in f:
            if aim in i:
                yield i


g = check_file('day14fuxi.py', '迭代器')
for i in g:
    print(i.strip())


# 4、 写生成器，从文件中读取内容之前，加上'***'之后再返回给用户
def check_file(filename):
    with open(filename, encoding='utf-8') as f:  # 句柄：handler，或文件操作符，文件对象
        for i in f:
            yield '***' + i


g = check_file('day14fuxi.py')
for i in g:
    print(i.strip())

# 看面试题
