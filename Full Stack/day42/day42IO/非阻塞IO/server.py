import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.setblocking(False)   # 吧socket当中所有需要阻塞的方法都改变非阻塞 recv recvfrom accept
sk.listen()

conn_l = []  # 用来存储所有来请求server端的conn连接
del_conn = []  # 用来存储所有已经断开与server端连接的conn
while True:
    try:
        conn, addr = sk.accept()  # 不阻塞，但是没人连我会报错
        print('建立连接了')
        # msg = conn.recv(1024)     # 不阻塞，但是没有消息会报错
        # print(msg)
        conn_l.append(conn)
    except BlockingIOError:
        for con in conn_l:
            try:
                msg = con.recv(1024)
                if msg == b'':
                    del_conn.append(con)
                    continue
                print(msg)
                con.send(b'bye')
            except BlockingIOError:pass

        for con in del_conn:
            conn_l.remove(con)
        del_conn.clear()