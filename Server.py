from socket import *
import os


HOST = 'localhost'
PORT = 8000


class Server:
    def __init__(self):

        with socket(AF_INET, SOCK_STREAM) as sock:

            sock.bind((HOST, PORT))
            sock.listen(5)
            print("Listening at {}:{}".format(HOST, PORT))

            while True:
                conn, addr = sock.accept()
                pid = os.fork()
                if pid == 0:
                    data = self.recv_all(conn)
                    print(data)

    def recv_all(self, conn):
        buffer: int = 1024
        msg: str = ''
        endl: bin = b'\r\n'
        chunk: bin = b''
        while endl not in chunk:
            chunk = conn.recv(buffer)
            msg += str(chunk)
        return msg




