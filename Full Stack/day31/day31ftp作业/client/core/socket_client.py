import json
import socket


class MySocketClient(object):
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1', 8080))

    def mysend(self, msg):
        ret_json = json.dumps(msg)
        self.sk.send(ret_json.encode('utf-8'))