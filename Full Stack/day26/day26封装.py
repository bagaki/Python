class Room(object):
    def __init__(self, name, length, width):
        self.__name = name
        self.__length = length
        self.__width = width

    def get_name(self):
        return self.__name

    def set_name(self, newName):
        if type(newName) is str and newName.isdigit() == False:
            self.__name = newName
        else:
            print('不合法姓名')

    def area(self):
        return self.__length * self.__width

kin = Room('kinsan', 2, 1.5)
print(kin.area())
kin.set_name('2')
print(kin.get_name())



# 假设父类的私有属性能被子类调用吗
class Foo(object):
    __kwy = '123'   # _Foo__kwy

class Son(Foo):
    print(Foo.__kwy)   # _Son__kwy

# 父类的私有属性，子类是调用不到的

# 会用到私有的这个概念的场景
# 1、隐藏起一个属性，不想让类的外部调用
# 2、想保护这个属性，不想让属性随意被改变
# 3、想保护这个属性，不被子类继承