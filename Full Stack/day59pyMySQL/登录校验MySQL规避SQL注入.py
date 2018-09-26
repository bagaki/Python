import pymysql


# 获取用户输入
username = input("Please input your name: ")
pwd = input("Please input your password: ")


# 连接数据库检索有没有该用户
conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    database = "userinfo",
    user = "root",
    password = "079450",
    charset = "utf8"
)

cursor = conn.cursor()
sql = "select * from info where username=%s and password=%s;"
ret = cursor.execute(sql, [username, pwd])  # 让pymysql帮我们拼接sql语句
if ret:
    print("success")
else:
    print("false")

cursor.close()
conn.close()