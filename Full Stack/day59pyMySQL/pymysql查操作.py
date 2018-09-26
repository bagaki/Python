"""
增操作
"""
import pymysql


conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    database = "userinfo",
    user = "root",
    password = "079450",
    charset = "utf8"
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 指定返回的数据格式为字典格式
sql = "select * from info;"

cursor.execute(sql)  # 返回的不是具体的数据，而是受影响的行数
# ret = cursor.fetchall()  # 返回所有数据
# ret = cursor.fetchone()
# print("{} rows in set.".format(ret))

# ret = cursor.fetchmany(3)
# print(ret)
# ret2 = cursor.fetchall()
# print(ret2)

# ret = cursor.fetchmany(3)
# print(ret)
# cursor.scroll(0, mode="absolute")  # 绝对移动，写多少就是移到多少
# ret2 = cursor.fetchall()
# print(ret2)

ret = cursor.fetchmany(3)
print(ret)
cursor.scroll(1, mode="relative")
ret2 = cursor.fetchall()
print(ret2)


cursor.close()
conn.close()