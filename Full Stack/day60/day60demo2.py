import pymysql


user = input("username:")
pwd = input("password: ")

conn = pymysql.connect(host='localhost', user='root', password='079450',db='school')
cursor = conn.cursor()

sql = 'select * from userinfo where username=%s and password=%s'
cursor.execute(sql,user,pwd)
result = cursor.fetchone()

cursor.close()
conn.close()