# 把解决一类问题的模块放在同一个文件夹里   ----- 包

import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py', 'w'))
# l.append(open('glance/api/__init__.py', 'w'))
# l.append(open('glance/api/policy.py', 'w'))
# l.append(open('glance/api/versions.py', 'w'))
# l.append(open('glance/cmd/__init__.py', 'w'))
# l.append(open('glance/cmd/manage.py', 'w'))
# l.append(open('glance/db/__init__.py', 'w'))
# l.append(open('glance/db/models.py', 'w'))
# map(lambda f:f.close(), l)


import glance.api.policy as policy
policy.get()

from glance.api import policy
policy.get()

import sys
sys.path.insert(0, r'D:\program\oldmantest\quanzhan\day21\dir')
from glance.api import policy
policy.get()

import glance
# 执行包下的__init__.py
glance.api.policy.get()


# 绝对路径 ，不管在包内部还是在外部都导入了就能用
# 不能挪动，但直观


from dir import glance
glance.api.policy.get()

# 相对路径
# 可以随意移动包，只要能找到包的位置，就可以使用包里的模块
# 包里的模块如果项使用其他模块的内容只能使用相对路径，使用了相对路径就不能在包内直接执行了

