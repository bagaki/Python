import socket


sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
ret = conn.recv(2)
ret1 = conn.recv(10)
print(ret)
print(ret1)

conn.close()
sk.close()