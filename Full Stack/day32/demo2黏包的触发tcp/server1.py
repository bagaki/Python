import socket


sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
ret = conn.recv(12)
print(ret)
ret1 = conn.recv(12)
print(ret1)

conn.close()
sk.close()



# Windows会发送一个空消息或直接报错

# 多个send，send小的数据连在一起，会发生黏包现象，是tcp协议内部的优化算法造成的
# 连续使用了send