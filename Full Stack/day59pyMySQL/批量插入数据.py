import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    database="userinfo",
    user="root",
    password="079450",
    charset="utf8"
)

cursor = conn.cursor()
# 创建班级的sql语句
sql = "insert into info(username, password) value (%s, %s);"

data = [("hide","000"),("yoshiki","111"), ("toshi","222"), ("pata","333"),("heath","444"),("sugizo","555"),("taiji","666")]

try:
    cursor.executemany(sql, data)  # 内部实现for循环
    # for i in data:
    #     cursor.execute(sql, i)
    conn.commit()
except Exception as e:
    print("Erroe!!")
    conn.rollback()

cursor.close()
conn.close()