# 接口类  抽象类
# python中没有接口类，有抽象类，abc模块中的metaclass = ABCMeta，abstructmethod
# 本质是做代码规范，希望在子类中实现父类方法名完全一样的方法
# 区别：在java的角度上看，是有区别的
#     java本来就支持单继承，所以就有了抽象类
#     java没有多继承，所以为了接口隔离原则，设计了接口这个概念，支持多继承
# python即支持单继承也支持多继承，所以对于接口类和抽象类的区别就不那么明显了
# 甚至在python中并没有内置接口类

# 多态和鸭子类型
# 多态 -- python天生支持多态
# 鸭子类型 -- 在不依赖父类的情况下实现两个相似的类中的同名方法

# 封装 -- 私有的
# 在python中只要__名字
# 在python中只要__名字，就把这个名字私有化了
# 私有化了之后，就不能从类的外部直接调用
# 静态属性 方法 对象属性 都可以私有化
# 这种私有化只是从代码级别做了变形，并没有真的约束
# 变形机制： _类名__名字，在类外用这个调用，在类的内部直接__名字调用