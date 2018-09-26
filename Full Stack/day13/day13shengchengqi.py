# 生成器函数 -- 本质上就是我们自己写的函数
def generator():
	print(1)
	return 'a'

ret = generator()
print(ret)

# 只要含有yield关键字的函数都是生成器函数
# yield不能和return 共用且需要写在函数内部
def generator():
	print(1)
	yield 'a'

# 生成器函数：执行之后会得到一个生成器作为返回值
ret = generator()
print(ret)
print(ret.__next__())
# ret.__iter__


def generator():
	print(1)
	yield 'a'
	print(2)
	yield 'b'
	yield 'c'

g = generator()

for i in g:
	print(i)

ret = g.__next__()
print(ret)
ret = g.__next__()
print(ret)
ret = g.__next__()
print(ret)

# 制作两千个哇哈哈
def wahaha():
	for i in range(20000):
		yield 'wahha{}'.format(i)

g = wahaha()
count = 0
for i in g:
	count += 1
	print(i)
	if count > 50:
		break

print('****', g.__next__())  # 可以接着继续往下走
# 或者
for i in g:
	count += 1
	print(i)
	if count > 100:
		break