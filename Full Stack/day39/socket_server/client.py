import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))


ret = sk.recv(1024).decode('utf-8')
print(ret)
msg = input('>>> ').encode('utf-8')
sk.send(msg)

sk.close()