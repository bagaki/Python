# 人狗大战
def Person(name, blood, aggr, sex):
	person = {
		'name':name,
		'blood': blood,
		'aggr':aggr,
		'sex':sex
	}
	# 人的技能 打
	def attack(dog):
		dog['blood'] -= person['aggr']
		print('{}被打了，掉了{}的血'.format(dog['name'], person['aggr']))

	person['attack'] = attack
	return person



def Dog(name, blood, aggr, kind):
	dog = {
		'name':name,
		'blood':blood,
		'aggr':aggr,
		'kind':kind
	}
	# 狗 咬人
	def bite(person):
		person['blood'] -= dog['aggr']
		print('{}被咬了，掉了{}的血'.format(person['name'], dog['aggr']))
	dog['bite'] = bite
	return dog


alex = Person('baga', 100, 1, None)
nezha = Person('nezha', 200, 2, None)
kin = Dog('Kinsan', 1000, 100, 'teddy')

# Dog函数和Person函数都是定义了一类事物
# 知道调用了函数，赋值之后才真的有实实在在的人或狗

# 面向对象编程
# 所谓模子 就是 类：抽象的，能知道有什么属性，有什么技能，但不能知道属性具体的值
# kin alex就是对象：有具体的值，属性和技能都是根据类规范的



class 类名:
	属性 = 'a'

print(类名.属性)


class Person(object):
	country = 'China'   # 创造了有一个只要事这个类就一定有的属性
	                    # 类属性  静态属性
	def __init__(self, name, hp, aggr, sex):  # 初始化方法，self事对象，事一个必须传的参数
		self.name = name
		self.hp = hp
		self.aggr = aggr
		self.sex = sex

	def walk(self):    # 方法，一般情况下，必须传self参数，且必须写在第一个，后面还可以传其他参数（自由的）
		print('%swalkwalkwalk'%self.name)

alex1 = Person('baga', 100, 1, None)  # 类名还可以实例化对象，alex对象
print(alex1.__dict__)  # 查看所有属性
print(Person.walk(alex1))
alex1.walk()
print(Person.country)  # 类名：可以查看类中的属性，不需要实例化就可以查看
print(Person.__dict__['country'])
print(alex1.__dict__['name'])
f = alex1.__dict__['name'] = 'cha'
print(f)

# 对象= 类名()
# 过程：
#     类名()：首先会创造除一个对象，创建一个self变量
#     调用init方法，类名括号里的参数会被这里接收
#     执行init方法
#     返回self

# self就是一个可以存储很多属性的大字典
# 往字典里添加属性的方式发生了一些变化

# 对象能做的事：
#     查看属性
#     调用方法
#     __dict__对于对象的增删改查操作都可以通过字典的语法进行

# 类名能做的事：
#     实例化
#     调用方法：只不过要自己传递self参数
#     调用类中的属性：调用静态属性
#     __dict__对于类中的名字只能看，不能操作
