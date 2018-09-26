import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

import socketserver
from core.server import MyftpServer

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyftpServer)
    server.serve_forever()