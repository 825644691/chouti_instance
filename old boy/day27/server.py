import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务器启动")
        conn = self.request
        print(self.client_address)
        while True:
            data = conn.recv(1024)
            if not data:break
            print(str(data,'utf8'))
            conn.sendall(data)
        conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),Myserver)
    server.serve_forever()