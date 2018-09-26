"""
不完善的web服务端示例
"""

import socket


sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(4)

while True:
    conn, addr = sk.accept()
    ret = conn.recv(8096)
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    conn.send(b'<h1>Hello</h1>')
    conn.close()
    sk.close()
