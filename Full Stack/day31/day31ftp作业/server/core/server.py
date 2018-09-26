import json
import socketserver
from core import views
from conf import settings


class MyftpServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.my_recv()
        # 消息的转发，把任务转给views文件中的对应的方法
        ope_str = msg['operation']
        if hasattr(views, ope_str):
            func = getattr(views, ope_str)
            ret = func(msg)
            self.my_send(ret)
        # {'username', 'passwd','operation'}
        # msg
        # 登录 注册
        # 查看目录
        # 上传文件
        # 反射
        #     'login'

    def my_recv(self):    # 派生方法
        msg = self.request.recv(1024)
        msg = msg.decode(settings.code)
        msg = json.loads(msg)
        return msg

    def my_send(self, msg):
        msg = json.dumps(msg).encode(settings.code)
        self.request.send(msg)
