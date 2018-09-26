import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

sk.send(b'hello')
sk.send(b'world')

import time
time.sleep(4)
sk.close()



# 优化算法
# 连续的小数据包，会被合并