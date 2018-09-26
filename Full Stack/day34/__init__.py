import socket


sk = socket.socket()
sk.setblocking(False)
sk.bind(('127.0.0.1', 8080))
sk.listen()

try:
    conn, addr = sk.accept()
except BlockingIOError:
    pass

print('*******')