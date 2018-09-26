# 正则表达式
# 字符组[字符]
# 元字符
#    \w  \d  \s
#    \W   \D   \S
#    .  除换行符以外所有字符
#    \n  \t
#    \b
#    ^ $ 匹配字符串的开始和结束
#    ()  分组  是对多个字符组整体量词约束的时候使用的
#              re模块：分组是有优先的
#              findall
#              split
#    |   从左到右匹配，只要匹配上就不继续匹配了，所以应该把长的放前面
#    [^]  除了字符组内的其他的都匹配
# 量词
#    *  零次或多次
#    +  一到多次
#    ?  零或一次
#    {n}   n次
#    {n, }  n到无穷大次
#    {n,m}  n到m次
# 转义：在匹配的时候出现特殊字符
# import re
# re.findall('\\s',r'\s')

# 惰性匹配
# 量词后面加文豪
# 尽量少的匹配
# .*?x  一只取，遇到x就停

# re模块
# import re
# re.findall('\d', 'ff322sg', re.S)
# 返回值：列表  列表中是所有匹配到的项

# ret = search('\d(\w)+', 'ff322sg')
# ret = search('\d(?P<name>\w)+', 'fhkhs3r')
# 找整个字符串，遇到匹配上的就返回，遇不到就None
# 如果有返回值ret.group()就可以取到值
# 去分组中的内容：ret.group(1) /  ret.group('name')

# match
# 从头开始匹配，匹配上了就返回，匹配不上就是None
# 如果匹配上了，group取值

# 分割 split
# 替换 sub 和subn
# finditer 返回迭代器
# compile 编译  在正则表达式很长且要多次使用，就必须要用编译