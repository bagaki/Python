from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0, path.dirname(getcwd()))
# 修改sys.path,把homework这个路径写道sys.path列表中
# 之后所有的模块导入，都是基于homework
from core import main
from core.school import *


if __name__ == '__main__':
    main.main()


# start文件
# 配置文件怎么用
# 登录成功之后使用反射来获取身份对应的类