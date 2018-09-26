# 写函数，检查获取传入列表或元组对象所有奇数位索引对应的元素，并将其作为新列表返回给调用者
def func(l):
	return l[1::2]
print(func([1,2,3,4,5]))


# 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def func1(x):
	return len(x)>5
print(func1('asdccff'))


# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
def func2(l):
	return l[:2]

print(func2([1,2,3,4]))


# 写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果
def func3(s):
	dic = {'num':0,'alpha':0, 'space':0, 'other':0}
	for i in s:
		if i.isdigit():
			dic['num'] += 1
		elif i.isalpha():
			dic['alpha'] += 1
		elif i.isspace():
			dic['space'] += 1
		else:
			dic['other'] += 1
	return dic

print(func3('03js+idnd9'))


# 谐函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容，并返回结果
def func4(x):
	if type(x) is str and x:
		for i in x:
			if i == ' ':
				return True
	elif x and type(x) is list or type(x) is tuple:
		for i in x:
			if not i :
				return True


# 写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留两个长度的内容，并将新内容返回给调用者
def func5(dic):
	for k in dic:
		if len(dic[k]) > 2:
			dic[k] = dic[k][:2]
	return dic

dic = {"k1":"v1v1", "k2":[11,22,33,44]}
print(func5(dic))



# 谐函数，接收两个数字参数，返回比较大的数字
def func6(a,b):
	if a > b:
		return a
	else:
		return b
print(func6(1,5))


# 三元运算
a = 1
b = 5
c = a if a>b else b
print(c)

def func7(a,b):
	return a if a > b else b


# 谐函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量此u该操作