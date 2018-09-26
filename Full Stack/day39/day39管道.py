# 什么是管道
from multiprocessing import Pipe, Process


# def func(conn):
#     conn.send('eat it')
#
#
# if __name__ == '__main__':
#     conn, conn1 = Pipe()
#     Process(target=func, args=(conn,)).start()
#     print(conn1.recv())


def func(conn, conn1):
    conn1.close()
    while True:
        try:
            msg = conn.recv()
            print(msg)
        except EOFError:
            conn.close()
            break



if __name__ == '__main__':
    conn, conn1 = Pipe()
    Process(target=func, args=(conn, conn1)).start()
    conn.close()
    for i in range(20):
        conn1.send('eat it')
    conn1.close()