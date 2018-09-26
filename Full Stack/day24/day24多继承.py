class F:
    def func(self):
        print('F')

class A(F):
    def func(self):
        print('A')
class B(A):
    def func(self):
        print('B')

class E(A):
    def func(self):
        print('E')

class C(E):
    def func(self):
        print('C')
class D(B,C):
    def func(self):
        print('D')

d = D()
d.func()
print(D.mro())

# 新式类 继承object类的才是新式类 ，广度优先
# 经典类：如果直接创建一个类再2.7中就是经典类，深度优先

# 多继承中，我们子类的对象调用一个方法，默认是就近原则，找的顺序是什么
# 经典类中，深度优先
# 新式类中，广度优先
# 2.7，新式类和经典类共存，新式类要继承object
# 3.0，只有新式类，默认继承object
# 经典类和新式类还有一个区别 super mro方法只在新式类中存在

# super的本质：不是单纯直接找父类，而是根据调用者的节点位置的广度优先顺序来的