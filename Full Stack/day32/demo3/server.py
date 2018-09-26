# 连续send两个小数据
# 两个recv，第一个recv特别小
# 远程执行命令的程序
# ipconfig --> 2000
# 2000 - 1024 = 976
# dir --> 200
# 200+976  -->  黏包

# 连续send两个小数据 2+8=10
#    2
#    8
# 两个recv，第一个recv特别小
#     recv（数据的长度）
# 本质，你不知道地道要接收多大的数据

# 解决
# 首先，发送一下这个数据到底有多大
# 再按照数据的长度接收数据

import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('>>>')
    if cmd == 'q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))
    num = conn.recv(1024).decode('utf-8')
    conn.send(b'ok')
    res = conn.recv(int(num)).decode('gbk')
    print(res)
conn.close()
sk.close()