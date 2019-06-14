import socket

sk =socket.socket()
print(sk)
address = ('127.0.0.1',8000)
sk.connect(address)

while True:
    inp = input(">>>")
    if inp == "exit":
        break
    sk.send(bytes(inp,'gbk'))
    result_len = int(str(sk.recv(1024),'utf8'))
    print(result_len)
    data = bytes()
    while len(data) != result_len:
        rec = sk.recv(700)
        data += rec

    print(str(data,'gbk'))


