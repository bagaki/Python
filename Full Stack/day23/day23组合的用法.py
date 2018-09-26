# 面向对象的三大特性：继承 多态 封装
# 组合
# 人狗大战
class Dog(object):
	def __init__(self, name, aggr, hp, kind):
		self.name = name
		self.aggr = aggr
		self.hp = hp
		self.kind = kink

	def bite(self, person):
		person.hp -= self.aggr

class Person(object):
	def __init__(self, name, attack, hp, sex, money):
		self.name = name
		self.attack = attack
		self.hp = hp
		self.sex = sex
		self.money = 0

	def bite(self, dog):
		dog.hp -= self.attack

	def get_weapon(self, weapon):
		if self.money >= weapon.price:
			self.money -= weapon.price
			self.weapon = weapon
			self.aggr += weapon.aggr
		else:
			print('余额不足')


class Weapon(object):
	"""docstring for Weapon"""
	def __init__(self, name, aggr, njd, price):
		self.name = name
		self.aggr = aggr
		self.njd = njd
		self.price = price

	def eighthand(self, person):
		if self.njd > 0:
			person.hp -= self.aggr
			self.njd -= 1
		

alex = Person('alex', 0.5, 100, None)
kin = Dog('alex', 100, 500, 'teddy')
w = Weapon('打狗棒', 100, 3, 998)

# alex装备大狗棒
alex.money += 1000
alex.get_weapon(w)
print(alex.weapon)
print(alex.aggr)

alex.attack(kin)
print(kin.hp)

alex.weapon.eighthand(kin)
print(kin.hp)

# 装备：
# 伤害
# 血量

# 组合：一个对象属性值是另外一个类的对象
#     alex.weapon是Weapon类的对象
