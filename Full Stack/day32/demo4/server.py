import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('>>>')
    if cmd == 'q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))
    num = conn.recv(4)   # 2048
    num = struct.unpack('i', num)[0]
    res = conn.recv(int(num)).decode('gbk')
    print(res)
conn.close()
sk.close()


# 如果发送数据的时候
# 先发送长度，先接收长度
# 在网络上传输的所有数据，都叫数据包
# 数据包里的所有数据，都叫报文
# 报文里不止有数据，还有ip地址 mac地址  端口号
# 所有的报文，都有报头
# 报头是协议规定的
# 所有的协议都会有报头
# 接收多少个字节等

# 自我定制报文
#     比如说，在一些复杂的应用上会用到
#         传输文件的时候就狗复杂
#             文件的名字在
#             文件的大小
#             文件的类型
#             存储的路径
head = {'filename':'test', 'filesize':409600, 'filetype':'txt', 'filepath':r'\user\bin'}
# 报头的长度                           # 先接收4个字节
# send(head)   # 自定制报头            # 根据这4个字节获取报头
# send(file)   # 报文                  # 从报头中获取filesize，然后根据filesize接收文件
# send(num+head)

# 其实在网络的传输的过程当中，处处有协议
# 协议就是一堆报文和报头 -- 字节
# 协议的解析过程我们不需要关心

# 如果跳出我们所了解的端口 ip 协议
# 我们写的程序也需要多次发送数据或者发送多个数据
# 我们也可以自定制协议 -- 本质上就是一种约定
