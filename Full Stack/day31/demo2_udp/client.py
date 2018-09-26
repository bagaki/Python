import socket


sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = (('127.0.0.1', 8080))

sk.sendto(b'hello', ip_port)
ret, addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))

sk.close()