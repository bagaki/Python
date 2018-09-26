import pymysql


user = input("username:")
pwd = input("password: ")

conn = pymysql.connect(host='localhost', user='root', password='079450',db='school')
cursor = conn.cursor()

cursor.execute('select * from class')
result = cursor.fetchone()
# 还有fetchmany(4)和fetchall

cursor.close()
conn.close()

if result:
    print('Login success')
else:
    print('Login false')