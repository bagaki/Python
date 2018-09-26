# 列表推导式
egg_list = ['egg{}'.format(i for i in range(10))]


egg_list = []
for i in range(10):
	egg_list.append('egg{}'.format(i))

print([i*i for i in range(10)])

# 生成器表达式
g = (i for i in range(10))
print(g)
for i in g:
	print(i)

# 括号不一样，
# 返回的值不一样 --- 不占用内存

egg_list = ('egg{}'.format(i for i in range(10)))
print(egg_list)
for egg in egg_list:
	print(egg)


g = ['10**2={}'.format(i*i for i in range(10))]
