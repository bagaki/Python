import pymysql


username = input("Please input your name:")
pwd = input("Please input your password:")


# 拿到用户输入的用户名密码

# 取数据库里判断用户名和密码是否正确
# 1.连接数据库
conn = pymysql.connect(host="localhost",
                port=3306,
                database="userinfo",
                user="root",
                password="079450",
                charset="utf8"
)

cursor = conn.cursor()  # 获取输入sql语句的光标对象
sql = "select * from info;"
ret = cursor.execute(sql)
print(ret)

cursor.close()
conn.close()

# 2.判断 --> 只需要把检索条件写到sql语句中，取数据库执行就可以了

# with open("userinfo", "r", encoding="utf-8")as f:
#     for line in f:
#         # print(line.strip())
#         u, p = line.strip().split("|")
#         if u == username and p == pwd:
#             print("success")
#             break
#     else:
#         print("get out")
