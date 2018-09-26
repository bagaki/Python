import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    info = input('>>>')
    sk.send(bytes(info, encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        sk.send(b'bye')
        break
    # sk.send(b'hi, world')
    # ret = sk.recv(1024)
    # print(ret)
    # sk.send(bytes('梨好'.encode('utf-8')))
    # ret = sk.recv(1024)
    # print(ret.decode('utf-8'))

sk.close()