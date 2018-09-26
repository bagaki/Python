import socket
from multiprocessing import Pool


def func(conn):
    conn.send(b'hello')
    ret = conn.recv(1024).decode('utf-8')
    print(ret)
    conn.close()


if __name__ == '__main__':
    p = Pool()
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()

    while True:
        conn, addr = sk.accept()
        p.apply_async(func, args=(conn, ))
    sk.close()