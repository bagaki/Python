import select
import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.setblocking(False)
sk.listen()


read_lst = [sk]
while True:
    rlist, wlist, xlist = select.select(read_lst, [], [])
    for i in rlist:
        if i is sk:
            conn,addr = i.accept()
            read_lst.append(conn)
        else:
            ret = i.recv(1024)
            if ret == b'':
                i.close()
                read_lst.remove(i)
                continue
            print(ret)
            i.send(b'bye')