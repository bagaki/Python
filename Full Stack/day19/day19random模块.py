import random
# 随机小数
# random.random()  # 大于0且小于1之间的小数
# random.unifor(1,3)  # 大于1小于3的小数

# # 随机整数
# random.randint(1, 5)   # 大于等于1且小于等于5之间的整数
# random.randrange(1, 10, 2)  # 大于等1且小于10之间的奇数

# # 随机选择一个返回
# random.choice([1,'23', [4,5]])  # 1或者23或者[4,5]
# # 随机选择多个返回，返回的个数为函数的第二个参数
# random.sample([1,'23', [4,5]], 2)  # 列表元素任意2个组合


# # 打乱列表顺序
# item = [1,3,5,7,9]
# random.shuffle(item)  # 打乱次序
# item


# 验证码
# 四到六个随机数字和字母
# random 正则
def check_num():
	checkCode = ''
	for i in range(6):  # 0
		c = random.randrange(0, 6)
		c1 = random.randrange(0, 6)
		if c == i:
			t = chr(random.randint(65, 90))
		elif c1 == i:
			t = chr(random.randint(97, 122))
		else:
			t = random.randint(0, 9)
		checkCode += str(t)
	return checkCode

print(check_num())