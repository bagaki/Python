import socket


sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('137.0.0.1', 8090))

msg,addr = sk.recvfrom(1024)

while True:
    cmd = input('>>> ')
    if cmd == 'q':
        break
    sk.sendto(cmd.encode('utf-8'), addr)
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))

sk.close()

# udp
# udp不会黏包
# 但会丢包