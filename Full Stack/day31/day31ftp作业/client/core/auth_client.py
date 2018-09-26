import socket
from core.socket_client import MySocketClient


class Auth(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        '''单例模式，为了防止重复登录连接'''
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self):
        self.socket = MySocketClient()
        self.username = None

    def login(self):
        username = input('username: ')
        passwd = input('password: ')
        if username.strip() and passwd.strip():
            self.socket.mysend({'username':username, 'password':passwd, 'operation':'login'})
        ret = self.socket.sk.recv(1024)   # 登录的结果

    def register(self):
        username = input('username: ')
        passwd = input('password: ')
        passwd1 = input('password_ensure: ')
        if username.strip() and passwd.strip() and passwd == passwd1:
            self.socket.mysend({'username':username, 'password':passwd, 'operation':'register'})
        ret = self.socket.sk.recv(1024)  # 注册的结果
