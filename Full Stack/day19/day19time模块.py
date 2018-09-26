import time
time.sleep(10)
print(time.time())

# 时间戳：从1970年1月1日凌晨开始
# 格式化的时间字符串（Format String）:'1999-12-06'
# 元组（struct_time)

# 字符串 --- 格式化时间，给人看的
# 时间戳 --- 计算机看的
# 结构化时间 --- 元组：计算用的

print(time.strftime("%Y-%m-%d %H:%M:%S"))

struct_time = time.localtime()
print(struct_time.tm_year)

# 时间戳和结构化时间
t = time.time()
print(time.localtime(t))
print(time.time(t))
print(time.mktime(time.localtime()))
time.striptime('2000-12.31', ''%Y-%m.%d)
time.strftime('%m/%d/%y %H:%M:%S', time.localtime(300000000))

print(time.asctime())