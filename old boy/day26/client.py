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
    s = sk.recv(1024)
    print(str(s,'gbk'))

