import socket


sk = socket.socket()
addr = ('127.0.0.1',8000)
sk.connect(addr)
print("客户端启动")
while True:
    inp = input('>>>')
    if inp == 'exit':
        print('聊天结束')
        break
    sk.sendall(bytes(inp,'utf8'))
    data_result = sk.recv(1024)
    print(str(data_result,'utf8'))
