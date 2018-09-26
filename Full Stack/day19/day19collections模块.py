# 列表、元组
# 字典
# 集合、frozenset
# 字符串
# 堆栈：先进后出
# 队列：先进先出


from collections import namedtuple


Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(p)


# 花色和数字
Card = namedtuple('card', ['suits','num'])
c1 = Card('red heart', 2)
print(c1)
print(c1.num)
print(c1.suits)


# deque 队列
import queue
q = queue.Queue()
q.put([1,2,3])
q.put(10)
q.put(5)
q.put(6)
print(q)  # 只有一个内存地址
# print(q.get())
# print(q.get())
# print(q.get())  # 阻塞
print(q.qsize())

# 双端队列
from collections import deque

dq = deque([1,2])
dq.append('a')       # 从后面放数据
dq.appendleft('b')   # 从前面放数据
dq.insert(2,3)
print(dq.pop())          # 从后面取数据
print(dq.popleft())      # 从前面取数据
print(dq)


# OrderedDict
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2),('c', 3)])
print(od)
print(od['a'])
for k in od:
	print(k)


# defaultdict
from collections import defaultdict
d = defaultdict(lambda :5)
print(d['k'])