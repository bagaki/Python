#  多态：python天生支持多态

# 多态指的是一类事物有多种形态
# 文件有多种形态：文本文件，可执行文件

# 多态性

# python动态强类型的语言
# 鸭子类型
# list tuple
# 不崇尚根据继承所得来的相似
# 我只是自己实现我自己的代码就可以了
# 如果两个类刚好相似，并不产生父类的子类的兄弟关系，而是鸭子类型
# index tuple 这种相似，是自己写代码的时候约束的，而不是通过父类的约束的
# 优点：松耦合，每个相似的类之间都没有影响
# 缺点：太随意了，只能靠自觉

class Lst(object):
    def __len__(self):pass
class Tple(object):
    def __len__(self):pass

def len(l_t):
    return l_t.__len__()

l = Lst()
len(l)

# 接口类和抽象类在python当中的应用点并不是非常必要
