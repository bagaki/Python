import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8000))
while True:
    msg = input('client1 >>> ')
    if msg == 'bye':
        sk.send(b'bye')
        break
    sk.send(('client1'+msg).encode('utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    print(ret)
sk.close()