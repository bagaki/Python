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
    sk.send(str(len(std_out)+len(std_err)).encode('utf-8'))
    sk.recv(1024)
    sk.send(std_out)
    sk.send(std_err)
sk.close()


# 好处：确定了我到底接收多大的数据
#       要在文件中配置一个配置项：就是每一次recv的大小  buffer=4096
#       当我们要发送大数据的时候，要明确的告诉接收方，要发送多大的数据，以便接收方能准确的接收到所有数据
#       多用在文件传输的过程中
#            大文件的传输，一定是按照字节读，每一次读固定的字节
#            传输的过程中，一边读一边传，接收端，一边收一边写
#            send大文件之前，35672字节 ，send(4096) 35672-4096-4096 --> 0
#            recv这个大文件，recv 35672字节，recv(2048)  35672 -2048 --> 0

# 不好的地方：多了一次交互
# send  sendto在超过一定范围的时候，都会报错
# 程序的内存管理
