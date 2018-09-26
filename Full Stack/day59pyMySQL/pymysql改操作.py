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

cursor = conn.cursor()
sql = "update info set password=%s where username=%s"
try:
    cursor.execute(sql, ["123","hide"])
    conn.commit()
except Exception as e:
    print("Error!: ", str(e))
    conn.rollback()   # 回滚

cursor.close()
conn.close()