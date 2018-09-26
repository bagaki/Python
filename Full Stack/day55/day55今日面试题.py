"""
问 字符串格式化：%和format 有什么区别

Python新版本推荐使用format.

python2.6 新加入的format语法支持

3.6新特性：
f-string
f"{name} is {age}"
"""

c = (250, 250)

command1 = "向它开炮：%s" % (c,)
print(command1)

command2 = "向它开炮：{}".format(c)
print(command2)

print(f"向它开炮：{c}")

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{self.name} is {self.age} years old".format(self=self)

p1 = Person("Alex", 9000)
print(p1)

date = [11, 22]
print("{0[0]} -- {0[1]}".format(date))

print("{:>10}".format(19))
print("{:0>10}".format(19))
print("{:s>10}".format(19))

# zfill
print("18".zfill(10))


print("{:.2f}".format(3.1415926))

print("{:,}".format(3442398329))