class Dog(object):
	def __init__(self, name, blood, aggr, kind):
		self.name = name
		self.blood = blood
		self.aggr = aggr
		self.kind = kind

	def bite(self, person):
		person.blood -= self.aggr


class Person(object):
	def __init__(self, name, blood, aggr, sex):
		self.name = name
		self.blood = blood
		self.aggr = aggr
		self.sex = sex

	def attack(self, dog):
		dog.blood -= self.aggr

kin = Dog('kinsan', 100, 20, 'teddy')
alex = Person('alex', 999, 998, None)
kin.bite(kin)
print(alex.blood)
