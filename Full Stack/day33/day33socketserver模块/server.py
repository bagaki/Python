# socket tcp
# socketserver tcp  与多个客户端连接
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):   # self.request 相当于conn
        # print(self.request.recv(1024).decode('utf-8'))
        while True:
            msg = self.request.recv(1024).decode('utf-8')
            if msg == 'q':
                # self.request.close()
                break
            print(msg)
            info = input('>>> ')
            self.request.send(info.encode('utf-8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    # thread 线程：在一个程序里，如果正常情况下，只会有一个线程，就是调度cup的最小调度
    server.serve_forever()


# bind、listen
# conn, addr = accept
# self.request = conn

# socket_server

# 看源码！！！！
# 第一，多个类之间的继承关系要先整理
# 每一个类中有哪些方法，要大致列出来
# 所有的self对象调用要清楚的了解，到底是谁的对象
# 所有的方法调用要退回到最子类的类中开始寻找，逐级向上
#