"""
完善的web服务端示例
函数版根据不同的路径返回不同的内容
进阶函数版，不写if判断了，用url名字去找对应的函数名
"""

import socket


sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(4)


# 定义一个处理/bagaki/的函数
def bagaki(url):
    ret = 'Hello, {}'.format(url)
    return bytes(ret, encoding="utf-8")


def tomoya(url):
    ret = 'Hello, {}'.format(url)
    return bytes(ret, encoding="utf-8")


while True:
    conn, addr = sk.accept()
    ret = conn.recv(8096)
    ret_str = str(ret, encoding="utf-8")
    l1 = ret_str.split("\r\n")
    print(l1[0])
    # 按照空格切割上卖弄的字符串
    l2 = l1[0].split()
    url = l2[1]
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    # 根据不同的url返回不同的内容
    if url == "/bagaki/":
        response = bagaki(url)
    elif url == "/tomoya/":
        response = tomoya(url)
    else:
        response = b'<h4>404! Not found!</h4>'
    conn.send(response)
    conn.close()
    sk.close()
