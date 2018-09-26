import time
import socket
import pymysql
from jinja2 import Template


def foo():
    """
    处理用户请求，并返回响应的内容
    :param request: 用户请求的所有信息
    :return:
    """
    f = open("index.html", "rb")
    data = f.read()
    f.close()
    return data


def bar():
    f = open("aricle.html", "r", encoding="utf-8")
    data = f.read()
    f.close()
    ctime = time.time()
    data = data.replace("@@sw@@", str(ctime))
    return bytes(data, encoding="utf-8")


def userlist(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', pwd='079450',db='userinfo')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open("aricle.html", "r", encoding="utf-8")
    data = f.read()
    f.close()

    template = Template(data)
    data = template.render(user_list=user_list)
    return data.encode('utf-8')


routers = [
    ('/foo', foo),
    ('/bar', bar),
    ('/userlist', userlist),
]

def run():
    sk = socket.socket()
    sk.bind(("127.0.0.1", 8080))
    sk.listen(5)

    while True:
        conn, addr =  sk.accept()
        data = conn.recv(8096)
        data = str(data, encoding="utf-8")
        headers, bodys = data.split("\r\n\r\n")
        temp_list = headers.split("\r\n")
        method, url, protocal = temp_list[0].split(" ")
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name()
        else:
            response = b"404"

        conn.send(response)
        conn.close()


if __name__ == "__main__":
    run()