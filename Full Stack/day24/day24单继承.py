# # 父类、基类、超类
# class A(object):
#     pass
#
#
# class B(object):
#     pass
#
#
# # 子类、派生类
# class A_son(A, B):
#     pass
#
#
# class AB_son(A, B):
#     pass
#
#
# # 一个类可以被多个类继承
# # 一个类 可以继承多个父类 -- 只在python里有多继承
# print(A_son.__bases__)
# print(AB_son.__bases__)
# print(A.__bases__)  # 没有继承父类默认继承object
#
#
# class Animal(object):
#     def __init__(self, name, aggr, hp):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#
#
# class Dog(Animal):
#     def bite(self, person):
#         person.hp -= self.aggr
#
#
# class Person(Animal):
#     pass
#
#
# kin = Dog('kin', 200, 500)
# print(kin.name)
#
#
# # 狗类
# # 鸟类
# class Animal(object):
#     def __init__(self):
#         print('执行Animal.__init__')
#         self.func()
#
#     def eat(self):
#         print('{} eating'.format(self.name))
#
#     def drink(self):
#         print('{} drinking'.format(self.name))
#
#     def func(self):
#         print(Animal.func)
#
#
# class Dog(Animal):
#     def guard(self):
#         print('guarding')
#
#     def func(self):
#         print('Dog.func')
#
#
# dog = Dog()
#
#
# class Bird(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def lay(self):
#         print('laying')
#
#
# bird = Bird()
#
# dog.drink()
# bird.drink()
# dog.guard()
# bird.lay()

class Animal(object):
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def eat(self):
        print('吃药')
        self.hp += 100


class Dog(Animal):
    def __init__(self, name, aggr, hp, kind):
        # Animal.__init__(self, name, aggr, hp)
        super().__init__(name, aggr, hp)
        self.kind = kind

    def eat(self):
        Animal.eat(self)   # 如果既想实现新的功能也想使用父类原本的功能，还需要在子类中再调用父类
        self.tooth = 2

    def bite(self, person):
        person.hp -= self.aggr


class Person(Animal):
    def __init__(self, name, aggr, hp, sex, money):
        Animal.__init__(self, name, aggr, hp)
        self.sex = sex
        money = 0

    def bite(self, dog):
        dog.hp -= self.aggr

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


kin = Dog('kin', 100, 500, 'teddy')
kin.eat()
print(kin.eat())
print(kin.hp)
alex = Person('alex', 1, 2, None, 1000)
alex.eat()
print(alex.hp)

kin.bite(alex)
print(alex.hp)

print(kin.name)
kin.eat()
super(Dog, kin).eat()


# 父类中没有的属性，在子类中出现，叫做派生属性
# 父类中没有的方法，在子类中出现，叫做派生方法
# 只要是子类的对象调用，子类中有的名字，一定用子类，子类中没有才找父类的，如果父类没有的报错
# 如果父类，子类都有，用子类的
# 如果还想用父类的，单独调用父类的:
#     父类名.方法名：需要自己传self参数
#     super().方法名：不需要自己传self

# 正常的代码中，单继承 === 减少了代码的重复
# 继承表达的是一种，子类是父类的关系
