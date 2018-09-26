"""
Python模拟链式操作
"""
class Foo(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def wang(self):
        print("wangwang")
        return self

    def run(self):
        print("dadada")
        return self


f = Foo("erge", 9000)
f.wang().run()
f.run()