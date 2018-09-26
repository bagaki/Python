# java：面向对象编程
# 设计模式 -- 接口类
# 接口类：python原生不支持
# 抽象类：python原生支持
from abc import abstractmethod, ABCMeta
class Paymen(metaclass=ABCMeta):  # 元类，默认的元类 type
    @abstractmethod
    def pay(self, money):pass
        # raise NotImplemented  # 没有实现这个方法
# 规范：接口类或者抽象类都可以
# 接口类：是默认多继承，接口类所有的方法都必须不能实现 -- java
# 抽象类：不支持多继承，抽象类中可以实现一些代码的实现 -- java


class Wechat(Paymen):
    def pay(self, money):
        print('pay {} yuan'.format(money))


class Alipay(Paymen):
    def pay(self, money):
        print('pay {} yuan'.format(money))


class Applepay(Paymen):
    def fuqian(self, money):
        print('apple pay {}'.format((money)))


def pay(pay_obj, money):  # 统一支付入口
    pay_obj.pay(money)


wechat = Wechat()
wechat.pay(100)
ali = Alipay()
ali.pay(200)
pay(wechat,100)
pay(ali, 200)