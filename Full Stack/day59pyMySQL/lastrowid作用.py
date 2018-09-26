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
sql = "insert into class(name) value (%s);"
# 创建学生的sql语句
sql1 = "insert into student(name, cid) values (%s, %s);"

# sql2 = "select id from class order by id desc limit 1;"

cursor.execute(sql, 'python_s9')
new_id = cursor.lastrowid  # 获取刚插入数据的id值
cursor.execute(sql1, ['bagaki',new_id])
conn.commit()

cursor.close()
conn.close()