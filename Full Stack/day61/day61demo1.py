import pymysql


user = input("username:")
pwd = input("password: ")

conn = pymysql.connect(host='localhost', user='root', password='079450',db='school', charset='utf8')
cursor = conn.cursor()  # 列表套字典
cursor.callproc('p1')
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