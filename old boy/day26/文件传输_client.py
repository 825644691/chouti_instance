import socket
import os



sk =socket.socket()
print(sk)
address = ('127.0.0.1',8000)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#命令行传输文件，要拿到命令，文件名，路径，文件大小
while True:
    inp = input(">>>")#post|11.png

    cmd,path = inp.split("|")

    path =os.path.join(BASE_DIR,path)#拼接路径

    filename = os.path.basename(path)#获取路径最后的文件名

    file_size = os.stat(path).st_size

    file_info = 'post|%s|%s' %(filename,file_size)
    sk.sendall(bytes(file_info,'utf8'))


    with open(path,'rb') as f:
        has_sent = 0
        while has_sent !=file_size:
            data = f.read()
            sk.sendall(data)
            has_sent +=len(data)

    print("上传成功")






