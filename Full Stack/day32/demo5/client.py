# 发送端
import os
import json
import struct
import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8090))
buffer = 4096

# 发送文件
head ={'filepath':r'D:\TOKIO\愛！wanne be with you', 'filename':r'04.Lowrider(BT).wma', 'filesize':None}
file_path = os.path.join(head['filepath'], head['filename'])
filesize = os.path.getsize(file_path)
head['filesize'] = filesize
json_head = json.dumps(head)   # 字典转为字符串
bytes_head = json_head.encode('utf-8')   # 字符串转bytes
# print(json_head)
# print(bytes_head)

# 计算head的长度
head_len = len(bytes_head)
pack_len = struct.pack('i', head_len)
# print(head_len, pack_len)
sk.send(pack_len)  # 先发报头的长度
sk.send(bytes_head)  # 再发送bytes类型的报头
with open(file_path, 'rb') as f:
    while filesize:
        if filesize >= buffer:
            content = f.read(buffer)   # 每次读出的内容
            sk.send(content)
            filesize -= buffer
        else:
            content = f.read(filesize)
            sk.send(content)
            break
sk.close()