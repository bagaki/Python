import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    conn.recv(1024)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    with open('data.txt', 'rb') as f:
        msg = f.read()
    conn.send(msg)
    conn.close()
