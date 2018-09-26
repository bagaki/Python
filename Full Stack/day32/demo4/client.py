import struct
import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    cmd = sk.recv(1024).decode('gbk')
    if cmd == 'q':
        break
    res = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = res.stdout.read()
    std_err = res.stderr.read()
    len_num = len(std_out)+len(std_err)
    num_by = struct.pack('i',len_num)
    sk.send(num_by)   # 4  2048
    sk.send(std_out)   # 1024
    sk.send(std_err)   # 1024
sk.close()


