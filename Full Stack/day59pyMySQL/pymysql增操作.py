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


# cursor = conn.cursor()
# sql = "insert into info(username, password) values ('mabo','101112');"
# cursor.execute(sql)
# conn.commit()
#
# cursor.close()
# conn.close()


# cursor = conn.cursor()
# sql = "insert into info(username, password) values (%s, %s);"
# cursor.execute(sql, ['ani', '131415'])
# conn.commit()
#
# cursor.close()
# conn.close()

# 报错
cursor = conn.cursor()
sql = "insert into info(username, password) values (%s, %s);"
try:
    cursor.execute(sql, ['ani', ])
    conn.commit()
except Exception as e:
    print("Error!: ", str(e))
    conn.rollback()   # 回滚

cursor.close()
conn.close()