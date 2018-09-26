import socket
from threading import Thread


# 子进程的input
# def demo(n):
#     info = input('{}: '.format(n))
#     print(info)
#
#
# for i in range(100):
#     t = Thread(target=demo, args=(i, ))
#     t.start()

# 默写
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


def chat(conn):
    conn.send(b'hello')
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()

while True:
    conn, addr = sk.accept()
    t = Thread(target=chat, args=(conn, ))
    t.start()

sk.close()