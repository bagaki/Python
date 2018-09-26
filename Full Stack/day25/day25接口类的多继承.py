from abc import abstractmethod, ABCMeta


class Swim_Animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

class Walk_Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class Fly_Animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass



class Swan(Fly_Animal, Walk_Animal, Swim_Animal):
    def walk(self):
        pass

    def fly(self):
        pass

    def swin(self):
        pass


class Oldying(Walk_Animal, Fly_Animal):
    def fly(self):
        pass

    def walk(self):
        pass

class Tiger(Walk_Animal, Swim_Animal):
    def walk(self):
        pass

    def swin(self):
        pass

# 接口类，刚好满足接口隔离原则，面向对象开发的思想，规范