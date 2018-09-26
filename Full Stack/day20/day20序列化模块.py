# 什么叫序列化 --- 将原本的字典、列表等内容转换成一个字符串的过程就叫序列化
# 序列化 --- 转向一个字符串数据类型
# 序列 --- 字符串

# 数据存储
# 网络上传输的时候

# 从数据类型 --->  字符串的过程 就叫序列化
# 从字符串 --- > 数据类型的过成 就叫反序列化

# json
# pickle
# shelve

# json 通用的序列化格式
#      只有很少的一部分数据类型能够通过json转化成字符串
# pickle
#     所有的python中的数据类型都可以转化成字符串形式
#     pickle序列化的内容只有python能理解
#     且部分反序列化依赖python代码
# shelve
#     序列化句柄
#     使用句柄直接操作，非常方便
#     

# json：dumps序列化方法  loads 反序列化方法
dic = {'k1':'v1'}
print(type(dic),dic)
import json
str_d = json.dumps(dic)   #序列化
print(type(str_d), str_d)

dic_d = json.loads(str_d)
print(type(dic_d),dic_d)

dic = (1,2,3,4)
print(type(dic),dic)
import json
str_d = json.dumps(dic)   #序列化
print(type(str_d), str_d)

dic_d = json.loads(str_d)
print(type(dic_d),dic_d)

# 数字 字符串 列表 字典 元组

# json  dump  load
dic = {1:'a', 2:'b'}   # dic = {1:'中国', 2:'b'}
f = open('fff', 'w',encoding='utf-8')
json.dump(dic, f)   # json.dump(dic, f, ensure_ascii=False)
f.close()

f = open('fff')
res = json.load(f)
res1 = json.load(f)
f.close()
print(type(res), res)
print(type(res1), res1)

# json
# dumps {} --> '{}\n'
# 一行一行的读
# 每一行字符串进行loads '{}\n'
# '{}' loads

# 存数据
l = [{'k':'111'},{'k1':'121'},{'k2':'113'}]
f = open('file', 'w')
for dic in l:
	str_dic = json.dumps(dic)
	f.write(str_dic + '\n')
f.close()

# 读数据
f = open('file')
l = []
for line in f:
	dic = json.loads(line.strip())
	l.append(dic)
f.close()
print(l)


# -----------------pickle------------
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  # 一串二进制内容

dic2 = pickle.loads(str_dic)
print(dic2)  # 字典

import time
struct_time = time.localtime(100000000)
print(struct_time)
f = open('pickle_file', 'wb')
pickle.dump(struct_time, f)
f.close()

f = open('pickle_file', 'rb')
struct_time2 = pickle.load(f)
print(struct_time2, tm_year)
f.close()

# 对于pickle来说，是可以序列化任何数据类型的
# 当pickle和所有文件打交道时，所有文件形式都要加b，wb,rb