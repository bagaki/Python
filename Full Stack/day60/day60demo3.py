import pymysql


user = input("username:")
pwd = input("password: ")

conn = pymysql.connect(host='localhost', user='root', password='079450',db='school')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 列表套字典

sql = "insert into class(caption) value('三年五班')"
cursor.execute(sql)

# 批量提交
cursor.executemany(sql)

# 添加修改删除都要有commit
conn.commit()
result = cursor.fetchone()

cursor.close()
conn.close()





# 新插入数据的自增ID：cursor.lastrowid
conn = pymysql.connect(host='localhost', user='root', password='079450',db='school')
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 列表套字典
cursor = conn.cursor()

sql = "insert into class(caption) value('三年五班')"
cursor.execute(sql)
conn.commit()
print(cursor.lastrowid)

cursor.close()
conn.close()