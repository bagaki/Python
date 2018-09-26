import re

ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
# 还可以咋分组zhong?<name>的形式给分组起名字
# 获取的匹配结果可以直接用group('name')拿到对应的值
print(ret.group('tag_name'))  # 结果：h1
print(ret.group())              # 结果：<h1>hello</h1>

ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# 如果不给组起名字，页k\序号来找到对应的组，表示要找的内容和前面的组内容一致
# 获取的匹配结果可以直接用group(序号)拿到对应的值
print(ret.group(1))
print(ret.group())   # 结果：<h1>hello</h1>


ret = re.findall(r"\d+\.\d+|(\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
print(ret)  # ['1', '-2', '60', '', '5', '-4', '3']
ret.remove("")
print(ret)  # ['1', '-2', '60', '5', '-4', '3']


# 首先得到一个字符串
# ret = '术式'
# 函数运行

# 去空格
# ret.split('')

# 先算括号里的：找括号里，没有其他括号
# ret.split('()')
# 得到一个没有括号的表达式，只有加减乘除  从左到右先找到第一个乘除法
# 所有的乘除法都做完了
# 计算加减
# 只有一个数了，就可以结束了
