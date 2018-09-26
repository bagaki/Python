import socket


sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
print(addr)
while True:
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    print(ret)
    info = input('>>>')
    conn.send(bytes(info, encoding='utf-8'))
    # ret = conn.recv(1024)
    # print(ret)
    # conn.send(b'hello world')
    # ret = conn.recv(1024)
    # print(ret.decode('utf-8'))
    # conn.send(bytes('苹果好'.encode('utf-8')))
conn.close()

sk.close()


# server
# client 10秒 time.time() 把时间戳时间发给server